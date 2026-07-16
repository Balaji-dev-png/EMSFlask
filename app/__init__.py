from flask import Flask
from flask_migrate import migrate
from config import Config

from app.routes.home import home_bp  # Import the home blueprint
from app.routes.emp import emp_bp  # Import the employee blueprint
from app.routes.department import depart_bp  # Import the department blueprint

from app.models import db  # Import the SQLAlchemy instance

from flask_migrate import Migrate

migrate = Migrate()  # Create a Migrate instance

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    
    db.init_app(app)


    migrate.init_app(app,db)


    app.register_blueprint(home_bp)  # Register the home blueprint
    app.register_blueprint(emp_bp)  # Register the employee blueprint
    app.register_blueprint(depart_bp)  # Register the department blueprint

    return app


