from flask import Blueprint, render_template
from app.models.employee import Employee
from app.models import db

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    try:
        total_employees = Employee.query.count()
        total_departments = db.session.query(Employee.department).distinct().count()
    except Exception:
        total_employees = 0
        total_departments = 0
        
    return render_template("home.html", total_employees=total_employees, total_departments=total_departments)