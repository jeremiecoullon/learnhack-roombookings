# -*- coding: utf-8 -*-
import os

WTF_CSRF_ENABLED = True
SECRET_KEY = "you-will-never-guess"


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSV_DATA_PATH = os.path.join(basedir, 'CSV')


# mail server settings
# MAIL_SERVER = 'smtp.googlemail.com'
# MAIL_PORT = 465
# MAIL_USE_TLS = False
# MAIL_USE_SSL = True
# with open('../RoomBookings_email_stuff.txt','r') as f:
#     email_stuff = f.read().split('\n')
# MAIL_USERNAME = email_stuff[0]
# MAIL_PASSWORD = email_stuff[1]

# admin list
ADMINS = ['jeremie.coullon@gmail.com']

# pagination
POSTS_PER_PAGE = 3

WOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50

# available languages
LANGUAGES = {
    'en': 'English',
    'es': 'Español'
}
