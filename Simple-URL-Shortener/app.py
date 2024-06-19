from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import string
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(200), unique=True, nullable=False)
    short_code = db.Column(db.String(6), unique=True, nullable=False)

    def __repr__(self):
        return f"URL('{self.original_url}', '{self.short_code}')"

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form['url']

    # Check if the URL already exists in the database
    url_entry = URL.query.filter_by(original_url=original_url).first()

    if url_entry:
        # If URL already exists, return its short URL
        short_url = request.url_root + url_entry.short_code
        return render_template('shortened.html', short_url=short_url)

    # Generate a random short code
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(6))

    # Create a new entry in the database
    new_url = URL(original_url=original_url, short_code=short_code)
    db.session.add(new_url)
    db.session.commit()

    # Construct the short URL
    short_url = request.url_root + short_code

    return render_template('shortened.html', short_url=short_url)

@app.route('/<short_code>')
def redirect_to_url(short_code):
    url_entry = URL.query.filter_by(short_code=short_code).first_or_404()
    return redirect(url_entry.original_url)

if __name__ == '__main__':
    app.run(debug=True)

