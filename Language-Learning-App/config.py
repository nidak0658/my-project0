import os

class Config:
    # Secret key for CSRF protection and session management
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'

    # SQLAlchemy database URI
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'database.db')
    
    # Silence the deprecation warning
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Email configuration (if needed)
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
