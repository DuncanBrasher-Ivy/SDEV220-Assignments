from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80), unique=True, nullable=False)
    publisher = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"{self.id}, {self.name}, {self.author}, {self.publisher}"

    def serialize(self) -> dict:
        return {"id": self.id,
                "name": self.name,
                "author": self.author,
                "publisher": self.publisher,
                }

@app.route('/')
def index():
    return 'Hello, welcome to the homepage!'

@app.route('/books')
def get_books():
    return {"books": [book.serialize() for book in Book.query.all()]}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id, description="Holy cow, batman!")
    return book.serialize()

@app.route('/books', methods=['POST'])
def add_book():
    dat = request.json
    book = Book(name=dat['name'], author=dat['author'], publisher=dat['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

@app.route('/books/<id>', methods=['PUT']) # TODO: This one is a bit broken at the moment
def put_book(id):
    book = Book.query.get(id)
    if book is not None:
        db.session.delete(book)

    dat = request.json
    book = Book(id=id, name=dat['name'], author=dat['author'], publisher=dat['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id, description="You look as if you\'ve seen a ghost!")
    db.session.delete(book)
    db.session.commit()
    return {"deleted": id}


def create_db() -> None: # The tutorial said to do this from the REPL, but I figured I'd do it here instead.
    app.app_context().push()
    db.create_all()

    book = Book(id=1, name="1984", author="George Orwell", publisher="Amazon Kindle, until the incident.")
    print(book)
    db.session.add(book)

    db.session.commit()


def main(args):
    if "create-db" in args:
        create_db()

if __name__ == "__main__":
    from sys import argv
    main(argv)

