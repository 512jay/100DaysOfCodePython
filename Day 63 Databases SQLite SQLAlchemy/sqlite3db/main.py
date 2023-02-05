from flask import Flask
from flask_sqlalchemy import SQLAlchemy as Sa

# create the extension
db = Sa()


# Define Models
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)


new_entry = Books()
new_entry.id = 1
new_entry.title = "Harry Potter"
new_entry.author = "J. K. Rowling"
new_entry.rating = 9.3

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../new-books-collection.db"
# initialize the app with the extension
db.init_app(app)

with app.app_context():
    db.create_all()
    db.session.add(new_entry)
    db.session.commit()


# ### Using SQLite database directly
# import sqlite3
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE,
#   author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
