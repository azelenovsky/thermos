import os
from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy



basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
bookmarks = []
app.config['SECRET_KEY'] = '\x99\xb3\x04\xfd\xd7$"nS\xfa\x1f/\x19\xcf\xda>\xa9\x8d\xf9?\x12\xcfz\xc8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
db = SQLAlchemy(app)

from forms import BookmarkForm
import models

bookmarks = []

def store_bookmark(url, description):
    bookmarks.append(dict(
        url = url,
        description = description,
        user = "Dre",
        date = datetime.utcnow()
    ))

#Used before DB
#def new_bookmarks(num):
#    return sorted(bookmarks, key = lambda bm: bm['date'], reverse = True)[:num]


#Mock login
def logged_in_user():
    return models.User.query.filter_by(username="DreZee").first()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', new_bookmarks=models.Bookmark.newest(5))


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        bm = models.Bookmark(user= logged_in_user(), url = url, description = description)
        db.session.add(bm)
        db.session.commit()
        #store_bookmark(url, description)
        flash("Stored '{}'".format(description))
        return redirect(url_for('index'))
    return render_template('add.html', form = form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'),500


#Application is now run exclusively from manage script.
# if __name__ == '__main__':
#    app.run(debug=True)
    #app.run()