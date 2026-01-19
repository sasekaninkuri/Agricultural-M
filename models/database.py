import os
from flask_pymongo import PyMongo

mongo = PyMongo()

def init_db(app):
    # Use environment variable for production, fallback to local for development
    app.config["MONGO_URI"] = os.environ.get("MONGO_URI", "mongodb://localhost:27017/SalonAdmin")
    mongo.init_app(app)
    return mongo.db
