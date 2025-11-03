# Lost_And_Find — Project File Structure

A comprehensive guide to the directory structure and organization of the Lost_And_Find Flask application.

---

## Directory Structure

```
Lost_And_Find/
│
├── app.py
├── Procfile
├── README.md
├── requirements.txt
├── zDataFlow-Diagram.png
├── zFileStructure.md
├── zFrequentCommands.txt
├── zHowFilesAreRelated(DEPENDENCY).md
├── zHowToRunFromScratch.md
│
├── instance/
│   ├── log.db
│   └── lost_items.db
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── test.js
│   └── src/
│       ├── 1.txt
│       ├── anirudh.jpg
│       ├── mohit.jpg
│       └── siddu.jpg
│
└── templates/
    ├── about.html
    ├── base.html
    ├── index.html
    ├── logs.html
    └── update.html
```

---

## Core Application Files

### `app.py`
Main Flask application containing routes, database connections, and template rendering logic. Interfaces with SQLite databases in the `instance/` directory.

### `Procfile`
Deployment configuration for Heroku and PythonAnywhere. Specifies the web server startup command using Gunicorn.

### `requirements.txt`
Python dependencies list including Flask, SQLAlchemy, and Gunicorn. Used for environment setup during deployment.

### `README.md`
Project introduction with setup instructions and overview. Essential reading for new contributors.

### `zDataFlow-Diagram.png`
Visual diagram illustrating the system's data flow from user input through database operations.

---

## Configuration & Documentation

### `zFileStructure.md`
This document. Provides complete breakdown of repository organization.

### `zFrequentCommands.txt`
Quick reference for commonly used development and deployment commands.

### `zHowFilesAreRelated(DEPENDENCY).md`
Documentation explaining inter-file dependencies and module interactions.

### `zHowToRunFromScratch.md`
Step-by-step setup guide for running the project in a fresh environment.

---

## Database Files (`instance/`)

### `log.db`
Stores system event and activity logs.

### `lost_items.db`
Primary SQLite database containing all user-submitted lost and found items.

---

## Static Assets (`static/`)

### CSS (`css/style.css`)
Application styles and layout definitions for all HTML pages.

### JavaScript (`js/test.js`)
Client-side JavaScript file (currently unused).

### Resources (`src/`)
Additional static resources including sample images and text files used in templates.

---

## Templates (`templates/`)

### `base.html`
Master layout template using Jinja2 inheritance. Contains common header, footer, and base styles.

### `index.html`
Main homepage and dashboard interface.

### `about.html`
Information page describing the project.

### `logs.html`
Displays system logs retrieved from `log.db`.

### `update.html`
Form interface for editing lost and found item details.

---

## Application Flow

1. User requests a URL route
2. `app.py` handles the request and queries database (`lost_items.db` or `log.db`)
3. Data is passed to appropriate template in `templates/`
4. Template inherits from `base.html` and applies styles from `static/css/style.css`
5. Rendered page is returned to user's browser

---

## Technical Specifications

- **Framework:** Flask
- **Database:** SQLite
- **Template Engine:** Jinja2
- **Web Server:** Gunicorn
- **Python Version:** 3.10+

---

**Project Author:** Mohit
