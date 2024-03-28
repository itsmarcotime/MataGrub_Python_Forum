from flask import Blueprint, render_template

auth_pages = Blueprint("auth_pages", __name__)

@auth_pages.route('/login', methods=['GET', 'POST'])
def do_login():
    msg = ''

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor.execute('SELECT * FROM accounts WHERE username=%s AND password=%s', (username, password))
        record = cursor.fetchone()

        if record:
            session['logged_in'] = True
            session['username'] = record[1]
            session['id'] = record[0]
            return redirect(url_for('home'))
        else:
            msg = 'Incorrect username or password. Try again!'
    return render_template('login.html', msg=msg)

@app.route('/register', methods=['GET', 'POST'])
def do_register():
    msg = ''

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # check if account exists in mysql
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        # if account exists show error && validation checks
        if account:
            msg = 'This account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'You did not use a correct email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Sorry, Username can only contain characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out all the feilds in the form!'
        else:
            # Need to hash password
            # Account doesnt exits && the form is filled out so creat the user
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password, email,))
            conn.commit()
            msg = 'You have successfully registered your account! Continue to login.'

    elif request.method == 'POST':
        msg = 'Please fill out the required fields.'

    return render_template('register.html', msg=msg)