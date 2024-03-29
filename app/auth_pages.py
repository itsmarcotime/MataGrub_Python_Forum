from flask import Blueprint, render_template

auth_pages = Blueprint("auth_pages", __name__)

@auth_pages.route('/login', methods=['GET', 'POST'])
def do_login():
    return render_template('login.html')

@auth_pages.route('/register', methods=['GET', 'POST'])
def do_register():
    return render_template('register.html')