from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(255), unique=True, nullable=False)
    author = db.Column(db.String(255), nullable=False)
    publisher = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"

@app.route("/")
def hello_world():
    return "<p>Hello, Earth!</p>"

@app.route('/books')
def get_books():
    books = Book.query.all()
    return jsonify({"books": [book.__repr__() for book in books]})
