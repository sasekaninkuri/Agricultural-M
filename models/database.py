import os
from flask_pymongo import PyMongo

mongo = PyMongo()

def init_db(app):
    mongo.init_app(app)
    return mongo

def get_db():
    # If we have an app context, mongo.db should work
    db = mongo.db
    if db is not None:
        return db
    
    # Fallback: get it directly from the client if configured
    if mongo.cx:
        # Try to get the database name from config
        from flask import current_app
        db_name = current_app.config.get('MONGO_URI', '').split('/')[-1].split('?')[0]
        if not db_name:
            db_name = 'SalonAdmin' # Default fallback
        return mongo.cx[db_name]
    
    return None
