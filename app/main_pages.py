from flask import Blueprint, render_template

main_pages = Blueprint("main_pages", __name__)

@main_pages.route('/')
def base_page():
    return render_template('base.html', the_title='Welcome to the Mata Forum Page!')

@main_pages.route('/home')
# @check_logged_in
def home():
    cursor.execute("SELECT * FROM articles")
    posts = cursor.fetchall()

    if posts:
        return render_template('home.html', username=session['username'], articles=posts)
    else:
        msg = 'No posts have been found. Click on create post!'
        return render_template('home.html', username=session['username'], msg=msg)