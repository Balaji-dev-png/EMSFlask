from flask import Flask
from flask_migrate import Migrate
from config import Config

from app.models import db
from app.routes.home import home_bp
from app.routes.emp import emp_bp
from app.routes.department import depart_bp

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    app.register_blueprint(home_bp)
    app.register_blueprint(emp_bp)
    app.register_blueprint(depart_bp)
    
    return app
