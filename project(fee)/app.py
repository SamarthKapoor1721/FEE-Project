from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your-secret-key'

def authenticate_user(username, password):
    # Replace this with your actual authentication logic, querying a database, etc.
    return username == "username" and password == 'password'

@app.route('/')
def home():
    if 'username' in session:
        return render_template('signup.htm', username=session['username'])
    return render_template('signup.htm')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']
        if authenticate_user(user, pwd):
            session['username'] = user
            return redirect(url_for('expenso'))
        else:
            return render_template('signup.htm', error='Invalid username or password')  # Render signup page with an error message
    return render_template('signup.htm')


@app.route('/expenso')
def expenso():
    return render_template('expenso.htm')  # Redirect to signup if the user is not logged in

@app.route('/login')
def login():
    render_template(url_for('signup'))
# Function to authenticate users - replace this with a secure authentication mechanism


if __name__ == '__main__':
    app.run(debug=True)
