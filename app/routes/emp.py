from flask import Blueprint, request, redirect, url_for, render_template

emp_bp = Blueprint('emp', __name__)

# @emp_bp.route('/employees')
# def employees():
#     return "<h1>Employee List</h1><p>This page will display a list of employees.</p>"

# @emp_bp.route('/employees/create')
# def create_emp():
#     return "<h1>Create Employee</h1><p>This page will allow you to create a new employee.</p>"

# @emp_bp.route('/employees/<int:emp_id>/update')
# def update_emp(emp_id):
#     return f"<h1>Update Employee {emp_id}</h1><p>This page will allow you to update employee with ID {emp_id}.</p>"

# @emp_bp.route('/employees/<string:emp_id>/delete')
# def delete_emp(emp_id):
#     return f"<h1>Delete Employee {emp_id}</h1><p>This page will allow you to delete employee with ID {emp_id}.</p>"

# @emp_bp.route('/employees/<string:emp_name>/<int:emp_id>')
# def emp_details(emp_name, emp_id):
#     return f"<h1>Employee Details for {emp_name}</h1><p>This page will display details for employee with ID {emp_id}.</p>"


# @emp_bp.route('/employees/filter')
# def filteremp():

#     department = request.args.get('department')
#     salary = request.args.get('salary')

#     return f"department: {department}, salary: {salary}"








# @emp_bp.route("/employee/department")
# def departmentpage():
#     return redirect(url_for("department.departmentRedirect"))



@emp_bp.route("/emp/register")
def empregister():
    return render_template("addemp.html")




@emp_bp.route("/emp")
def emppage():


    employee_list = Employee.query.all()
    return render_template("employee.html", employee_list = employee_list)




from app.models.employee import Employee
from app.models import db


@emp_bp.route("/emp/add", methods = ["POST"])
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