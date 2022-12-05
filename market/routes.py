from market import app
from flask import render_template, redirect, url_for, flash, request, get_flashed_messages
from market.models import Item, User
from market.forms import RegisterForm
from market import db


@app.route('/')
@app.route('/home')
def index():
    return render_template('dashboard/home.html')

@app.route('/about/<username>')
def about_page(username):
    return f'The About Page for {username}'

@app.route('/market')
def market_page():
    items = Item.query.all()
#     items = [
#     {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
#     {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
#     {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
# ]
    return render_template('dashboard/market.html', **locals())

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data, email_address=form.email_address.data,password_hash=form.password.data)
        db.session.add(user_to_create)
        db.session.commit()
        flash(f'Account created successfully! You are now able to log in', category='success')
        return redirect(url_for('market_page'))
    if form.errors != {}: # if there are no errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
        

    return render_template('dashboard/register.html', **locals())