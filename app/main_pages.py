from flask import Blueprint, render_template

main_pages = Blueprint("main_pages", __name__)

@main_pages.route('/home')
def home():
    return render_template('test.html')