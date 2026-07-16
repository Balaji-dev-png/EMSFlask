from flask import Flask
from routes.home import home_bp  # Import the home blueprint
from routes.emp import emp_bp  # Import the employee blueprint
from routes.department import depart_bp  # Import the department blueprint


app = Flask(__name__) # app is the main file

app.register_blueprint(home_bp)  # Register the home blueprint
app.register_blueprint(emp_bp)  # Register the employee blueprint
app.register_blueprint(depart_bp)  # Register the department blueprint


if __name__ == "__main__":
    app.run(debug=True)