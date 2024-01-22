#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# if __name__== '__main__':
@app.route('/')
def index():
    return '<h1>Welcome to my page</h1>'

#variable routes
@app.route('/<string:username>')
def user(username):
    return f'<h1>Hello, {username}!</h1>'

@app.route('/about')
def about():
    w= f"<h1>About page</h1>"
    x= f"<p>Hello sir welcome to our about page"
    return f"{w} \n {x}"

if __name__== '__main__':
    app.run(port=5555, debug=True)
