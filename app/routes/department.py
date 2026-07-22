from flask import Blueprint, render_template
from app.models.employee import Employee
from app.models import db

depart_bp = Blueprint('department', __name__)

@depart_bp.route("/depart")
def depart():
    try:
        departments = db.session.query(
            Employee.department, 
            db.func.count(Employee.id)
        ).group_by(Employee.department).all()
    except Exception:
        departments = []

    return render_template("department.html", departments=departments)