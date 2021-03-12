from flask import Flask, render_template, redirect
from users import users
app = Flask(__name__)
users = users()

@app.route('/')
def index():
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)