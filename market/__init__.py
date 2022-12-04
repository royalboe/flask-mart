from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

from market import routes
from market import models