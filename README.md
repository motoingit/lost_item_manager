<!-- ======================================================================= -->
<!--? PROJECT: Lost and Found Management System -->
<!--? Author: Mohit | Date: October 2025 -->
<!--? Description: Modern Flask-based web app for managing lost & found items -->
<!-- ======================================================================= -->

<div align="center">
  <img src="https://img.icons8.com/fluency/96/lost-and-found.png" alt="Lost and Found Logo" width="100">
  <h1><strong>Lost and Found Management System</strong></h1>
  <p>
    A simple yet powerful web application built with Flask to manage lost and found items.<br>
    It provides an intuitive interface for reporting, searching, and managing items — featuring undo/redo, detailed logging, and intelligent sorting.
  </p>

<!-- PROJECT BADGES -->
  <p style="text-align:center; margin:20px 0;">
    <a href="#" style="pointer-events:none; cursor:default; text-decoration:none; margin:0 5px;">
      <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask Badge"/>
    </a>
    <a href="#" style="pointer-events:none; cursor:default; text-decoration:none; margin:0 5px;">
      <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite Badge"/>
    </a>
    <a href="#" style="pointer-events:none; cursor:default; text-decoration:none; margin:0 5px;">
      <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>
    </a>
  </p>

<<<<<<< HEAD
<p>
  <a href="#-installation-and-setup"><strong>🚀 Get Started</strong></a> • 
  <a href="#-features"><strong>✨ Features</strong></a> • 
  <a href="#-tech-stack"><strong>🧠 Tech Stack</strong></a> • 
  <a href="#-core-logic"><strong>⚡ Core Logic</strong></a> • 
  <a href="#-api-endpoints"><strong>🌐 API Endpoints</strong></a> • 
  <a href="#-contributors"><strong>👥 Contributors</strong></a> • 
  <a href="#-contact-details"><strong>📬 Contact</strong></a> • 
  <a href="#-salutations"><strong>🫡 Salutation's</strong></a>
</p>


=======
  <p>
    <a href="#-installation-and-setup"><strong>🚀 Get Started</strong></a> • 
    <a href="#-features"><strong>✨ Features</strong></a> • 
    <a href="#-contact"><strong>📬 Contact</strong></a>
  </p>
>>>>>>> 6245551042c98fd5cb79bcbe072c7ac01e6c8b41
</div>

---

## ✨ Features
- **Report Lost Items:** Easily log lost items with title and description.  
- **Advanced Search:** Search by ID, title, or keywords with database-level filtering.  
- **Flexible Sorting:** Sort items by title or date (ascending/descending).  
- **CRUD Operations:** Add, edit, view, and delete lost items seamlessly.  
- **Undo/Redo Stack:** Instantly revert or reapply recent actions using a stack-based algorithm.  
- **Action Logging:** Every action is tracked in a separate database for auditability.  
- **Timezone-Aware Timestamps:** All entries are recorded in IST (India Standard Time).  

---

## 🧠 Tech Stack

<div align ="left">
  <table border="1" cellspacing="0" cellpadding="6">
    <tr>
      <th>🧩 Layer</th>
      <th>🛠️ Technologies</th>
    </tr>
    <tr>
      <td><b>Backend</b></td>
      <td>Python, Flask</td>
    </tr>
    <tr>
      <td><b>Database</b></td>
      <td>SQLite</td>
    </tr>
    <tr>
      <td><b>ORM</b></td>
      <td>Flask-SQLAlchemy</td>
    </tr>
    <tr>
      <td><b>Frontend</b></td>
      <td>HTML5, Jinja2</td>
    </tr>
    <tr>
      <td><b>Deployment</b></td>
      <td>Gunicorn, dotenv</td>
    </tr>
  </table>
</div>

## ⚙️ Installation and Setup

Follow these steps to run the project locally:

### 1️⃣ Clone the Repository

  ```bash
  git clone <your-repository-url>
  ```

  ```bash
  cd <repo-folder>
  ```

---

### 2️⃣ Create a Virtual Environment

#### 🪟 For Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### 🍎 For macOS / 🐧 Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Initialize the Database

```bash
flask init-db
```

---

### 5️⃣ Run the Application

```bash
flask run
```

---

### Optional : Access the Application

After running, open this URL in your browser:

  ```
    http://127.0.0.1:5000
  ```

---

## ⚡ Core Logic

### 🧩 Stack for Undo/Redo
- Every operation is pushed to an **ActionStack**.  
- Undo → Pops last operation and reverses it.  
- Redo → Reapplies previously undone action.  
- All operations are **O(1)** — efficient and consistent.

### 🗄️ Search and Sort
- Search → SQLAlchemy `filter` + `contains()` for keyword queries.  
- Sort → SQL `ORDER BY` for database-level sorting (optimized on indexed fields).  

---

## 🌐 API Endpoints

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

## Markdown Stucture :
``` md
└── 📁Repo1-LostandFound
    └── 📁instance
        ├── log.db
        ├── lost_items.db
    └── 📁static
        └── 📁css
            ├── popup.css
            ├── style.css
        └── 📁js
            ├── popup.js
            ├── test.js
        └── 📁src
            ├── alok.jpg
            ├── anirudh.jpg
            ├── contrib_alok.txt
            ├── contrib_anirudh.txt
            ├── contrib_mohit.txt
            ├── contrib_ritik.txt
            ├── contrib_siddharth.txt
            ├── mohit.jpg
            ├── ritik.jpg
            ├── siddu.jpg
    └── 📁templates
        ├── about.html
        ├── base.html
        ├── index.html
        ├── logs.html
        ├── update.html
    ├── app.py
    ├── README.md
    └── requirements.txt
```

---

<!-- ## 👥 Contributors
<a href="https://github.com/othneildrew/Best-README-Template/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=othneildrew/Best-README-Template" alt="contrib.rocks image" />
</a> -->

## 👥 Contributors

<p align ="center">
  <a href="https://github.com/motoingit/" target="_blank">
    <img src="https://tse2.mm.bing.net/th/id/OIP.BtzFhDnkG0lVPsrzv93TywHaE8?rs=1&pid=ImgDetMain&o=7&rm=3" 
        width="80" height="80"
        alt="User1"
        style="border-radius: 50%; object-fit: cover; border: 2px solid #000000ff;">
  </a>
  <a href="https://github.com/motoingit/" target="_blank">
    <img src="https://th.bing.com/th/id/OIP.IGNf7GuQaCqz_RPq5wCkPgHaLH?o=7rm=3&rs=1&pid=ImgDetMain&o=7&rm=3" 
        width="80" height="80"
        alt="User1"
        style="border-radius: 50%; object-fit: cover; border: 2px solid #000000ff;">
  </a>
  <a href="https://github.com/motoingit/" target="_blank">
    <img src="https://tse4.mm.bing.net/th/id/OIP.NGfztPBkW4-18NnAVGC7CwHaGb?w=1200&h=1042&rs=1&pid=ImgDetMain&o=7&rm=3" 
        width="80" height="80"
        alt="User1"
        style="border-radius: 50%; object-fit: cover; border: 2px solid #000000ff;">
  </a>
  <a href="https://github.com/motoingit/" target="_blank">
    <img src="https://th.bing.com/th/id/R.3bcbeff4ee0abb81ef150c9ea7e35730?rik=t3aMo1m4uUQi6g&riu=http%3a%2f%2fwww.newdesignfile.com%2fpostpic%2f2010%2f05%2ffree-stock-photos-people_102217.jpg&ehk=vGjIrntn5QyP%2fIXY2Ei7Iiz4%2fy%2byXvP8I8j0XxemwjI%3d&risl=&pid=ImgRaw&r=0" 
        width="80" height="80"
        alt="User1"
        style="border-radius: 50%; object-fit: cover; border: 2px solid #000000ff;">
  </a>
</p>

---

## 📬 Contact Details

Stay connected and explore my work through the following platforms:

[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/your_username)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/your_username)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtube.com/@your_username)
[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://facebook.com/your_username)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:your_email@example.com)
[![Phone](https://img.shields.io/badge/Call-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](tel:+911234567890)

---

## 🌐 Other Platforms

[![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/your_username)
[![HackerEarth](https://img.shields.io/badge/HackerEarth-323754?style=for-the-badge&logo=hackerearth&logoColor=white)](https://www.hackerearth.com/@your_username)
[![GitHub](https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/your_username)

---

## 🫡 Salutation's

**Author:** *Mohit*  
**Date:** *October 2025*

<hr>
  <p align="center" style="color:#00bfa5; font-style:italic; font-size:16px;">
  🧭 Because every lost item has a story — and every story deserves a return.
  </p>
<hr>

---

<!-- ======================================================================= -->
<!--? END OF FILE | README.MD STRUCTURED WITH PROFESSIONAL VISUAL HIERARCHY -->
<!--? Designed for clarity, presentation, and GitHub optimization -->
<!-- ======================================================================= -->
