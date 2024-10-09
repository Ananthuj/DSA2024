from flask import Flask, render_template, request, session, url_for, redirect


app = Flask(__name__)
app.secret_key = 'your_secret_key'

users = {'username': 'password'}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        session['username'] = username
        return redirect(url_for('home'))
    else:
        return render_template('index.html', error='Invalid Login')
    return render_template('index.html')


@app.route('/home')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
