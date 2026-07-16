from flask import Flask
from app import create_app
from app.routes.home import home_bp  # Import the home blueprint
from app.routes.emp import emp_bp  # Import the employee blueprint
from app.routes.department import depart_bp  # Import the department blueprint

app = create_app()


if __name__ == "__main__":
    app.run(debug=True)