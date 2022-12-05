from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '0db6200689199ec18f0e1cf9'
db = SQLAlchemy(app)

from market import routes
from market import models