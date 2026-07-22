from flask import Blueprint, request, redirect, url_for, render_template
from app.models.employee import Employee
from app.models import db

emp_bp = Blueprint('emp', __name__)

@emp_bp.route("/emp/register")
def empregister():
    return render_template("addemp.html")

@emp_bp.route("/emp")
def emppage():
    search = request.args.get('search', '')
    search_by = request.args.get('search_by', 'name')
    
    filter_department = request.args.get('department', '')
    min_salary = request.args.get('min_salary', type=float)
    max_salary = request.args.get('max_salary', type=float)
    
    sort_by = request.args.get('sort_by', 'id')
    sort_order = request.args.get('sort_order', 'asc')
    
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

    query = Employee.query

    if search:
        if search_by == 'name':
            query = query.filter(Employee.name.ilike(f'%{search}%'))
        elif search_by == 'email':
            query = query.filter(Employee.email.ilike(f'%{search}%'))
        elif search_by == 'department':
            query = query.filter(Employee.department.ilike(f'%{search}%'))

    if filter_department:
        query = query.filter(Employee.department == filter_department)
    
    if min_salary is not None:
        query = query.filter(Employee.salary >= min_salary)
    
    if max_salary is not None:
        query = query.filter(Employee.salary <= max_salary)

    if sort_by == 'name':
        sort_column = Employee.name
    elif sort_by == 'email':
        sort_column = Employee.email
    elif sort_by == 'department':
        sort_column = Employee.department
    elif sort_by == 'salary':
        sort_column = Employee.salary
    else:
        sort_column = Employee.id

    if sort_order == 'desc':
        query = query.order_by(sort_column.desc())
    else:
        query = query.order_by(sort_column.asc())

    pagination = query.paginate(page=page, per_page=per_page, error_out=False)

    departments_result = db.session.query(Employee.department).distinct().all()
    departments = [d[0] for d in departments_result if d[0]]

    return render_template(
        "employee.html", 
        pagination=pagination,
        departments=departments
    )



@emp_bp.route("/emp/add", methods = ["POST", "GET"])
def addemp():
    if request.method == "POST":
        employee = Employee (
            name = request.form["name"],
            email = request.form["email"],
            department = request.form["department"],
            salary = request.form["salary"]
        )


        db.session.add(employee) # to create query to add data to the database
        db.session.commit() # to run the query on the server


        return redirect(url_for("emp.emppage")) # to redirect to the employee page after adding the employee



    return render_template("addemp.html")



@emp_bp.route("/emp/empdetail/<int:emp_id>", methods = ["GET"])
def empdetail(emp_id):

    employee = Employee.query.get_or_404(emp_id)

    return render_template("emp_detail.html", employee = employee)




@emp_bp.route("/emp/empdelete/<int:emp_id>")
def empdelete(emp_id):

    employee = Employee.query.get_or_404(emp_id)

    db.session.delete(employee)
    db.session.commit()

    return redirect(url_for("emp.emppage"))