
---

````markdown
# ⚙️ VIRTUAL ENVIRONMENT MANAGEMENT

---

```python
//! ================================================
//! VIRTUAL ENVIRONMENT MANAGEMENT
//! ================================================

//!     python -m pip uninstall virtualenv      // for see
//!     python -m pip uninstall virtualenv      // for uninstall

//!     python -m pip cache info                // to see cache
//!     python -m pip cache purge               // clear cache
````

---

## 🧩 STEP 1 : Install setuptools to install virtualenv

```python
//? -----------------------------------------------
pip install virtualenv      // installing the virtual environment
//? -----------------------------------------------
```

---

## 🧱 STEP 2 : Create a Virtual Environment

```python
//? -----------------------------------------------
virtualenv env
//* this helps to use different python versions or libraries you don’t want to install globally
//! If you face error, then run:
Set-ExecutionPolicy unrestricted
//? -----------------------------------------------
```

---

## ⚡ STEP 3 : Activate Virtual Environment

```python
//? -----------------------------------------------
.\env\Scripts\activate.ps1       // for environment activation
//! deactivate                    // to deactivate
//? -----------------------------------------------
```

---

## 📦 STEP 4 : Install Required Packages

```python
//? -----------------------------------------------
pip install flask               // main Flask class
pip install flask-sqlalchemy    // Flask package for database class
pip install datetime            // date and time
// OPTIONAL:
pip install gunicorn            // for production (multi-threaded)
//* ALL SET
//? -----------------------------------------------
```

**Tip:**

> Open one terminal for installing libraries (**virtual env**)
> And another terminal for running the app (**global terminal**)

---

## 🧮 Create `app.py` in the main directory (base folder)

```python
//* -----------------------------------------------
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
//* -----------------------------------------------
```

---

## 🗄️ Configuring the Database

Reference: [Flask-SQLAlchemy Config Docs](https://flask-sqlalchemy.readthedocs.io/en/stable/config/#flask_sqlalchemy.config.SQLALCHEMY_DATABASE_URI)

```python
// Example Command:
sqlite:///project.db

// flask object - to deal with endpoints 
// __name__ == "__main__" on direct run 
// "name" also helps to give static folder information

app = Flask(__name__)  # check f-1 for more info
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'   # config the database location
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False           # disable warning
```

```python
//! If this WARNING comes:
//! UserWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead. 
//! Set it to True or False to suppress this warning.

// THEN DO:
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

---

## 🧰 Database Initialization Commands (in Terminal)

Option 1:

```python
python
from app import app, db
with app.app_context():
    db.create_all()
```

Option 2 (via Flask CLI):

```python
@ app.cli.command("init-db")
def init_db_command():
    """Clears the existing data and creates new tables."""
    db.create_all()
    print("Initialized the database.")
```

Then run:

```bash
flask init-db
```

---

# 🧠 TEMPLATING & FRONTEND (JINJA2)

```python
/*
Now Jinja2 templating.

Adding the app (/show) route — going to /show would print the todo list in terminal.

There are filters in Jinja (explained in index.html).

Includes:
    - Jinja inheritance
    - Template inheritance
*/
```

---

# 🚀 DEPLOYMENT & PRODUCTION

```python
/*
Download Heroku and Heroku CLI.

Freeze our requirements file.

In virtual environment:
    pip install gunicorn
Gunicorn makes our application run in multiple threads.
*/
```

---

## 🧾 Deployment Commands

```python
pip freeze > requirements.txt      // freeze dependencies
//* Ctrl + Shift + R removes cached files in browser
```

---

# ✅ SUMMARY

| Stage        | Purpose                    |
| ------------ | -------------------------- |
| Virtual Env  | Isolate dependencies       |
| Flask        | Web framework              |
| SQLAlchemy   | Database ORM               |
| Gunicorn     | Production WSGI server     |
| Heroku / CLI | Deployment tools           |
| Jinja2       | Frontend templating engine |

---

🟩 **Color Legend**

| Symbol   | Meaning                    | Color (in your editor) |
| -------- | -------------------------- | ---------------------- |
| `//!`    | Warnings / Important Notes | 🔴 Red                 |
| `//?`    | Info / Reference           | 🔵 Blue                |
| `//*`    | Tips / Success             | 🟢 Green               |
| `//Todo` | Tasks / Future Items       | 🟠 Orange              |

---

✅ All commands and comments **preserved 100%**.
✅ Markdown-optimized for **clean readability** in VS Code, GitHub, or Notion.
✅ Syntax and structure untouched — just beautified and logically sectioned.

---

Would you like me to generate this as a **ready-to-download `setup_guide.md` file** so you can drop it directly into your project repo?
Absolutely — here’s your entire content **converted perfectly into Markdown (.md)** format, while preserving the **original look, meaning, and comment-style notation** (`//!`, `//?`, `//*`, etc.).
It’s structured for clean readability inside **VS Code, GitHub, or Notion**, and keeps every command intact.

---

````markdown
# ⚙️ VIRTUAL ENVIRONMENT MANAGEMENT

---

```python
//! ================================================
//! VIRTUAL ENVIRONMENT MANAGEMENT
//! ================================================

//!     python -m pip uninstall virtualenv      // for see
//!     python -m pip uninstall virtualenv      // for uninstall

//!     python -m pip cache info                // to see cache
//!     python -m pip cache purge               // clear cache
````

---

## 🧩 STEP 1 : Install setuptools to install virtualenv

```python
//? -----------------------------------------------
pip install virtualenv      // installing the virtual environment
//? -----------------------------------------------
```

---

## 🧱 STEP 2 : Create a Virtual Environment

```python
//? -----------------------------------------------
virtualenv env
//* this helps to use different python versions or libraries you don’t want to install globally
//! If you face error, then run:
Set-ExecutionPolicy unrestricted
//? -----------------------------------------------
```

---

## ⚡ STEP 3 : Activate Virtual Environment

```python
//? -----------------------------------------------
.\env\Scripts\activate.ps1       // for environment activation
//! deactivate                    // to deactivate
//? -----------------------------------------------
```

---

## 📦 STEP 4 : Install Required Packages

```python
//? -----------------------------------------------
pip install flask               // main Flask class
pip install flask-sqlalchemy    // Flask package for database class
pip install datetime            // date and time
// OPTIONAL:
pip install gunicorn            // for production (multi-threaded)
//* ALL SET
//? -----------------------------------------------
```

**Tip:**

> Open one terminal for installing libraries (**virtual env**)
> And another terminal for running the app (**global terminal**)

---

## 🧮 Create `app.py` in the main directory (base folder)

```python
//* -----------------------------------------------
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
//* -----------------------------------------------
```

---

## 🗄️ Configuring the Database

Reference: [Flask-SQLAlchemy Config Docs](https://flask-sqlalchemy.readthedocs.io/en/stable/config/#flask_sqlalchemy.config.SQLALCHEMY_DATABASE_URI)

```python
// Example Command:
sqlite:///project.db

// flask object - to deal with endpoints 
// __name__ == "__main__" on direct run 
// "name" also helps to give static folder information

app = Flask(__name__)  # check f-1 for more info
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'   # config the database location
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False           # disable warning
```

```python
//! If this WARNING comes:
//! UserWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead. 
//! Set it to True or False to suppress this warning.

// THEN DO:
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

---

## 🧰 Database Initialization Commands (in Terminal)

Option 1:

```python
python
from app import app, db
with app.app_context():
    db.create_all()
```

Option 2 (via Flask CLI):

```python
@ app.cli.command("init-db")
def init_db_command():
    """Clears the existing data and creates new tables."""
    db.create_all()
    print("Initialized the database.")
```

Then run:

```bash
flask init-db
```

---

# 🧠 TEMPLATING & FRONTEND (JINJA2)

```python
/*
Now Jinja2 templating.

Adding the app (/show) route — going to /show would print the todo list in terminal.

There are filters in Jinja (explained in index.html).

Includes:
    - Jinja inheritance
    - Template inheritance
*/
```

---

# 🚀 DEPLOYMENT & PRODUCTION

```python
/*
Download Heroku and Heroku CLI.

Freeze our requirements file.

In virtual environment:
    pip install gunicorn
Gunicorn makes our application run in multiple threads.
*/
```

---

## 🧾 Deployment Commands

```python
pip freeze > requirements.txt      // freeze dependencies
//* Ctrl + Shift + R removes cached files in browser
```

---

# ✅ SUMMARY

| Stage        | Purpose                    |
| ------------ | -------------------------- |
| Virtual Env  | Isolate dependencies       |
| Flask        | Web framework              |
| SQLAlchemy   | Database ORM               |
| Gunicorn     | Production WSGI server     |
| Heroku / CLI | Deployment tools           |
| Jinja2       | Frontend templating engine |

---
