from flask import Blueprint, render_template

depart_bp = Blueprint('department', __name__)

# @depart_bp.route('/department')
# def department():
#     return "<h1>this is my department page</h1>"

# @depart_bp.route('/department/sales')
# def sales():
#     return "<h1>this is my sales page</h1>"

# @depart_bp.route('/department/address')
# def address():
#     return "<h1>this is my address page</h1>"



@depart_bp.route("/depart")
def depart():
    return render_template("department.html")