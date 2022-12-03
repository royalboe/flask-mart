from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/about/<username>')
def about_page(username):
    return f'The About Page for {username}'