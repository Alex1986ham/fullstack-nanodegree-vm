from flask import Flask
from flask import render_template, flash, redirect
import os
from forms import LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import db
basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
#app.config.from_object(Config)
app.config['SECRET_KEY'] = 'you-will-never-guess'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# from app import routes, models



@app.route('/')
@app.route('/catalog')
def catalog():
    user = {'username': 'Alex'}
    posts = [
    {
        'author': {'username': 'John'},
        'body': 'Beautiful day in Portland!'
    },
    {
        'author': {'username': 'Susan'},
        'body': 'The Avengers movie was so cool!'
    }
    ]
    return render_template('catalog.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('catalog'))
    return render_template('login.html', title='Login', form=form)

@app.route('/catalog/<int:id>')
def category(id):
    return "this will work on a specific id"



class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-nerver-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)


if __name__ == '__main__':
        app.debug = True
        app.run(host='0.0.0.0', port=5000)
