from thermos import app, db
from flask.ext.script import Manager, prompt_bool

from models import User

manager = Manager(app)

@manager.command #Decorator makes this available on command line
def initdb():
    db.create_all()
    db.session.add(User(username = "DreZee", email = "dr@example.com"))
    db.session.add(User(username = "DiddleZero", email = "dizzle@example.com"))
    db.session.commit()
    print ("Database initialized")


@manager.command
def dropdb():
    if prompt_bool(
        "Are you sure you want to lose all your data"):
        db.drop_all()
        print("Dropped DB")

if __name__ == '__main__':
    manager.run()
