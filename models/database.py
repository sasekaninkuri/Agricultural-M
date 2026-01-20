import os
from flask_pymongo import PyMongo

mongo = PyMongo()

def init_db(app):
    # Use the URI already set in config.py
    mongo.init_app(app)
    return mongo.db
