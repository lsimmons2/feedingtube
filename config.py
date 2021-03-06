import os
# Define app directory
APP_ROOT = os.path.abspath(os.path.dirname(__file__))

# Don't let users run arbitrary Python code in production
DEBUG = False

# Use Gmail for our SMTP email server
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_DEFAULT_SENDER = 'no-reply@feedingtube.host'
