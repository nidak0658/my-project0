from datetime import datetime
from flask_login import UserMixin
from app import db, login_manager

# Define User model for authentication
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

# Define Lesson model
class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Lesson {}>'.format(self.title)

# Define Quiz model
class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    correct_answer = db.Column(db.String(100), nullable=False)
    wrong_answer1 = db.Column(db.String(100), nullable=False)
    wrong_answer2 = db.Column(db.String(100), nullable=False)
    wrong_answer3 = db.Column(db.String(100), nullable=False)
    explanation = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '<Quiz {}>'.format(self.question)

# Define Progress model
class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=True)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('progress', lazy=True))
    lesson = db.relationship('Lesson', backref=db.backref('progress', lazy=True))
    quiz = db.relationship('Quiz', backref=db.backref('progress', lazy=True))

    def __repr__(self):
        return '<Progress User:{} Lesson:{}>'.format(self.user_id, self.lesson_id)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
