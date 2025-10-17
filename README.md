# Lost and Found Management System

A simple yet powerful web application built with Flask to manage lost and found items. It provides a user-friendly interface to report, search, and manage items, incorporating features like undo/redo and detailed logging.

## Implemented

crud operations are - create read update delete

## Features

- **Report Lost Items**: Easily add new lost items with a title and description.
- **Advanced Search**: Search for items by ID, title, or a general text search across title and description.
- **Flexible Sorting**: Sort the item list by creation date or item title in ascending or descending order.
- **CRUD Operations**: Full Create, Read, Update, and Delete functionality for lost items.
- **Undo/Redo**: Revert or re-apply actions like adding, updating, or deleting items, powered by a stack data structure.
- **Action Logging**: All significant actions are logged into a separate database for auditing and tracking purposes.
- **Timezone-Aware Timestamps**: All timestamps are recorded in IST (India Standard Time) for consistency.

## Tech Stack

- **Backend**: Python, Flask
- **Database**: SQLite
- **ORM**: Flask-SQLAlchemy
- **Frontend**: HTML, Jinja2 Templating

## Installation and Setup

Follow these steps to get the application running on your local machine.

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <repository-folder>
    ```

2.  **Create a virtual environment:**
    It's recommended to use a virtual environment to manage project dependencies.
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    Create a `requirements.txt` file with the following content:
    ```
    Flask
    Flask-SQLAlchemy
    pytz
    ```
    Then, install the packages:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Initialize the database:**
    The application uses two SQLite databases. Initialize them using the custom Flask CLI command.
    ```bash
    flask init-db
    ```
    This will create an `instance` folder containing `lost_items.db` and `log.db`.

5.  **Run the application:**
    ```bash
    flask run
    ```
    The application will be available at `http://127.0.0.1:5000`.

## How It Works

### Data Structures and Algorithms

*   **Stack for Undo/Redo (`ActionStack`)**:
    -   Every action (add, update, delete) is pushed onto a stack as a dictionary containing the action type and relevant data.
    -   **Undo**: Pops the last action from the stack and performs the inverse operation (e.g., deletes an added item).
    -   **Redo**: Moves a pointer forward in the stack to re-apply a previously undone action.
    -   This provides O(1) time complexity for push, undo, and redo operations.

*   **Database-driven Search and Sort**:
    -   **Search**: Instead of a manual linear search in Python, the application leverages the power of the database. It uses SQLAlchemy's `filter` with `contains` for efficient text-based searching (`LIKE` queries in SQL). Searching by a primary key (`sno`) is even faster.
    -   **Sort**: Sorting is also delegated to the database using `ORDER BY` clauses, which is highly optimized, especially on indexed columns like `date_created` and `title`.

### API Endpoints

| Method | Endpoint          | Description                                                  |
|--------|-------------------|--------------------------------------------------------------|
| `GET`  | `/`               | Displays all lost items. Supports search and sort queries.   |
| `POST` | `/`               | Adds a new lost item to the database.                        |
| `GET`  | `/update/<sno>`   | Shows a form to edit an existing item.                       |
| `POST` | `/update/<sno>`   | Submits the updated item details.                            |
| `GET`  | `/delete/<sno>`   | Deletes an item from the database.                           |
| `GET`  | `/undo`           | Reverts the most recent action.                              |
| `GET`  | `/redo`           | Re-applies the most recently undone action.                  |
| `GET`  | `/about`          | Displays the About page.                                     |
| `GET`  | `/logs`           | Shows a list of all logged system actions.                   |

---

*Author: Mohit*
*Date: October 2025*