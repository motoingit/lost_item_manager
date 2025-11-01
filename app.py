"""
Lost and Found Management System (by flask)

It provides functionality to :
    1. Report lost items
    2. Search for lost items using linear search
    3. Update item status
    4. Track item history
    5. Maintain logs of all actions
    6. Undo/Redo operations using stack data structure
    7. sorting list by x way

Devloped By Team - Stubborn Spirit's
Date initiation : September 2025
Date deployment : Novmber 2025

"""

from flask import Flask, render_template, request, redirect
from datetime import datetime #
import pytz                   #
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
# def undo(self) -> Dict[str, Any] | None:
# def undo(self) -> Optional[Dict[str, Any]]:
""" both commnets are same"""
from typing import List, Optional, Dict, Any 

app = Flask(__name__)
#! app.config.from_object('config.Config')

# Stack implementation for undo/redo operations
class ActionStack:
    """
    #?(list)actions = [{'type': 'insert', 'value': 'A'}, {'type': 'insert', 'value': 'B'}]
    #?(list[x])action = {'type': 'insert', 'value': 'A'}

    """
    def __init__(self):
        self.actions: List[Dict[str, Any]] = []
        self.position: int = -1
        print("\nStack Initialized\n")
    
    #if i undo and then write some data/ it will trim the redos
    def push(self, action: Dict[str, Any]) -> None: # -> None is the return type
        # Clear any redo actions
        """
        data = ['A', 'B', 'C', 'D']
        print(data[:2])   # ['A', 'B']
        print(data[1:3])  # ['B', 'C']
        print(data[2:])   # ['C', 'D']

        """
        self.actions = self.actions[:self.position + 1]
        self.actions.append(action) # add the data to stack (LIST FUCTION)
        self.position += 1
    
    def undo(self) -> Dict[str, Any] | None:
        if self.position >= 0:
            action = self.actions[self.position]
            self.position -= 1
            print("\none action is undo\n")
            return action
        print("\nNo more actions to undo\n")
        return None
    
    def redo(self) -> Dict[str, Any] | None:
        if self.position + 1 < len(self.actions):
            self.position += 1
            return self.actions[self.position]
        return None

# Global action stack instance
action_stack = ActionStack()

# Configure instance path / database path
#__file__ == path of current  file its written
"""
#! os.path.dirname(__file__) is removing file form the directory
#! 💡 Think of it like this:
#!          mkdir → makes one door only.
#!          makedirs → builds the whole hallway if needed.
#!    
#!          makedirs → builds the whole hallway if needed.

"""
app.config['INSTANCE_PATH'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance')
os.makedirs(app.config['INSTANCE_PATH'], exist_ok=True)


#'sqlite:///lost_item.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.config['INSTANCE_PATH'], 'lost_items.db')
#? additional dataabase
app.config['SQLALCHEMY_BINDS'] = { 'log': 'sqlite:///' + os.path.join(app.config['INSTANCE_PATH'], 'log.db') }
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Set timezone to IST for consistent timestamps
#! ist is signalling const value or (one time initiated), although any variable can do the job
IST = pytz.timezone('Asia/Kolkata')

class LostItem(db.Model):
    """
    Model for lost items in the system.
    
    Attributes:
        sno: Unique identifier for the item
        title: Name or brief title of the lost item
        desc: Detailed description of the item
        date_created: Timestamp when the item was reported

    """
    # a tuple in Python is a fixed, ordered collection of elements, kind of like a list that you can’t modify once created.
    #? t = (10, "hello", 3.14)
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=lambda: datetime.now(IST))
#! So yes — it auto-increments linearly, not circularly. Once sno = 3, it won’t go back to 1 unless you reset the database.
    def __repr__(self) -> str:
        return f"Item #{self.sno} - {self.title}"

class Log(db.Model):
    __bind_key__ = 'log'
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(10), nullable=False)
    message = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(IST))

    def __repr__(self):
        return f"[{self.timestamp}] [{self.level}] [{self.message}]"

def log_message(level, message):
    log = Log(level=level, message=message)
    db.session.add(log)
    db.session.commit()

# some terminal commanes
#! flask run
#? export FLASK_ENV=devlopment or production
@app.cli.command("init-db")
def init_db_command():
    #! Initialize the database.
    try:
        db.create_all()
        print("Initialized the database.")
    except Exception as e:
        print(f"Error initializing database: {e}")

@app.route("/", methods=['GET', 'POST'])
def index():
    """
    Main route handling both display of lost items and addition of new items.
    
    GET: Display lost items with search and sort functionality
    POST: Add a new lost item to the system
    """
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        if title:  # Basic validation
            item = LostItem(title=title, desc=desc)
            print(item) #! initiate __repr__
            db.session.add(item)
            db.session.commit()
            # Store action for undo
            action_stack.push({
                'type': 'add',
                'item_id': item.sno,
                'data': {'title': title, 'desc': desc}
            })
            log_message('INFO', f'New lost item reported: {title}')
            return redirect('/')

    # Get search parameters
    search_query = request.args.get('search', '')
    search_by = request.args.get('search_by', 'all')
    sort_by = request.args.get('sort_by', 'date_desc')

    # Build the query
    query = LostItem.query

    # Apply search filters
    if search_query:
        log_message('INFO', f'Searched for lost item: {search_query} by {search_by}')
        if search_by == 'id':
            try:
                sno = int(search_query)
                query = query.filter(LostItem.sno == sno)
            except ValueError:
                # If the search query is not a valid integer, return no results
                return render_template('index.html', allItems=[])
        elif search_by == 'title':
            query = query.filter(LostItem.title.contains(search_query))
        else:  # search_by == 'all'
            query = query.filter(or_(
                LostItem.title.contains(search_query),
                LostItem.desc.contains(search_query)
            ))

    # Apply sorting
    if sort_by == 'date_asc':
        query = query.order_by(LostItem.date_created.asc())
    elif sort_by == 'date_desc':
        query = query.order_by(LostItem.date_created.desc())
    elif sort_by == 'name_asc':
        query = query.order_by(LostItem.title.asc())
    elif sort_by == 'name_desc':
        query = query.order_by(LostItem.title.desc())

    # Execute query
    all_items = query.all()
    return render_template('index.html', allTodo=all_items)

@app.route("/update/<int:sno>", methods=['GET', 'POST'])
def update(sno):
    """
    Update details of a lost item.
    
    GET: Display update form for the item
    POST: Save updated item details
    """
    item = db.session.get(LostItem, sno)
    if not item:
        log_message('WARNING', f'Attempted to update non-existent item #{sno}')
        return redirect('/')

    if request.method == 'POST':
        old_title = item.title
        old_desc = item.desc
        title = request.form['title']
        desc = request.form['desc']
        if title:  # Basic validation
            item.title = title
            item.desc = desc
            db.session.commit()
            # Store action for undo
            action_stack.push({
                'type': 'update',
                'item_id': sno,
                'old_data': {'title': old_title, 'desc': old_desc},
                'new_data': {'title': title, 'desc': desc}
            })
            log_message('INFO', f'Updated lost item #{sno}: {title}')
        return redirect('/')

    return render_template('update.html', todo=item)

@app.route("/delete/<int:sno>")
def delete(sno):
    """Delete a lost item from the system."""
    item = db.session.get(LostItem, sno)
    if item:
        # Store action for undo before deleting
        action_stack.push({
            'type': 'delete',
            'item_id': sno,
            'data': {'title': item.title, 'desc': item.desc}
        })
        db.session.delete(item)
        db.session.commit()
        log_message('INFO', f'Deleted lost item #{sno}: {item.title}')
    return redirect('/')

@app.route("/undo")
def undo():
    """Undo the last action using stack data structure."""
    action = action_stack.undo() # returing a list variable
    if action:
        if action['type'] == 'add':
            # Undo an add operation by deleting
            item = db.session.get(LostItem, action['item_id'])
            if item:
                db.session.delete(item)
                db.session.commit()
        
        elif action['type'] == 'delete':
            # Undo a delete operation by re-adding
            item = LostItem(sno=action['item_id'], **action['data'])
            db.session.add(item)
            db.session.commit()
        
        elif action['type'] == 'update':
            # Undo an update operation by restoring old data
            item = db.session.get(LostItem, action['item_id'])
            if item:
                item.title = action['old_data']['title']
                item.desc = action['old_data']['desc']
                db.session.commit()
        
        log_message('INFO', f'Undo operation: {action["type"]}')
    return redirect('/')

@app.route("/redo")
def redo():
    """Redo the last undone action using stack data structure."""
    action = action_stack.redo()
    if action:
        if action['type'] == 'add':
            # Redo an add operation by re-adding
            item = LostItem(sno=action['item_id'], **action['data'])
            db.session.add(item)
            db.session.commit()
        
        elif action['type'] == 'delete':
            # Redo a delete operation by deleting again
            item = db.session.get(LostItem, action['item_id'])
            if item:
                db.session.delete(item)
                db.session.commit()
        
        elif action['type'] == 'update':
            # Redo an update operation by applying new data
            item = db.session.get(LostItem, action['item_id'])
            if item:
                item.title = action['new_data']['title']
                item.desc = action['new_data']['desc']
                db.session.commit()
        
        log_message('INFO', f'Redo operation: {action["type"]}')
    return redirect('/')

@app.route("/about")
def about():
    """Render the about page with information about the Lost and Found system."""
    return render_template('about.html')

@app.route("/logs")
def logs():
    """Display system logs showing all actions and their timestamps."""
    all_logs = Log.query.all()
    print(all_logs)
    return render_template('logs.html', all_logs=all_logs)

if __name__ == '__main__':
    print("I'm On Main\n")
    #? default
    #! print(app.config) #! run it
    app.run(debug=True) # devlopment mode : on(python app.py) || off(flask run)
