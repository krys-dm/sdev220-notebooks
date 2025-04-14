from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from flask import request

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120))
    
    def __repr__(self):
        return f"{self.name} by {self.author}"

@app.route('/')
def index():
     return 'Hello!'
 
@app.route('/books')
def get_books():
    books = Book.query.all()
    
    output = []
    for book in books:
        book_data = {'name': book.name, 'author': book.author}
        output.append(book_data)
        
    return {"books": output}

@app.route('/books/<int:id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify({"name": book.name, "author": book.author})


@app.route('/books', methods=['POST'])
def add_book():
    book = Book(name=request.json['name'], author=request.json['author'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "not found"}, 404
    db.session.delete(book)
    db.session.commit()
    return {"message": "Book deleted"}
