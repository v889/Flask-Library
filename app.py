from flask import Flask, render_template

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from  database import db
from model import  Book
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SECRET_KEY'] = 'your_secret_key'


db.init_app(app)

def create_db():
    with app.app_context():
        db.create_all()

# Create Flask-Admin instance
admin = Admin(app, name='Library Admin', template_mode='bootstrap3')

# Add administrative views
admin.add_view(ModelView(Book, db.session))

# Route to display list of books using Jinja2 templates
@app.route('/books')
def list_books():
    books = Book.query.all()
    return render_template('index.html', books=books)

if __name__ == '__main__':
    from model import Book
    create_db()
    app.run(debug=True)
