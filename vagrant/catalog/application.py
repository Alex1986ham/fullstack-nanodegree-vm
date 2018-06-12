from flask import Flask
from flask import render_template, flash, redirect
import os
from forms import LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'



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
    if form.validaton_on_submit():
        flash('Login requested for user {}, remember_me={}.format(
            form.username.data, form.remember_me.data))
        return redirect('/catalog')
    return render_template('login.html', title='Login', form=form)

@app.route('/catalog/<int:id>')
def category(id):
    return "this will work on a specific id"



class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-nerver-guess'





if __name__ == '__main__':
        app.debug = True
        app.run(host='0.0.0.0', port=5000)
