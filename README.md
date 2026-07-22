# Employee Management System (EMS)

This is a Flask-based CRUD application extended with advanced data management features, built using Python, Flask, SQLAlchemy, and Bootstrap.

## Features Added
- **Pagination**: Navigate through records (5 or 10 per page).
- **Searching**: Search employees by Name, Email, or Department.
- **Sorting**: Order records by ID, Name, Email, Department, or Salary (Ascending/Descending).
- **Filtering**: Filter by specific Department and a custom Salary Range (Min/Max).
- **UI Enhancements**: Fully responsive Bootstrap UI, empty state handling, and clean grid layouts for forms.

## Prerequisites
- Python 3.8+
- MySQL Server

## Setup Instructions

1. **Clone the repository** (or navigate to the project directory):
   ```bash
   git clone https://github.com/Balaji-dev-png/EMSFlask
   cd EMSFlask
   ```

2. **Set up a Virtual Environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Database**:
   - Create a MySQL database named `ems_db`.
   - Update `config.py` with your MySQL credentials:
     ```python
     SQLALCHEMY_DATABASE_URI = "mysql+pymysql://<username>:<password>@localhost:3306/ems_db"
     ```

5. **Run Database Migrations** (if applicable) or create the tables manually via Python shell:
   ```python
   from app import create_app
   from app.models import db
   app = create_app()
   with app.app_context():
       db.create_all()
   ```

6. **Run the Application**:
   ```bash
   python app.py
   ```
   The application will be running at `http://127.0.0.1:5000/`.
