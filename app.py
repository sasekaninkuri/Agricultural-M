import os
from flask import Flask
from models.database import init_db
from routes.auth import auth_bp
from routes.services import services_bp
from routes.management import mgmt_bp
from routes.main import main_bp
from config import config

def create_app(config_name=None):
    application = Flask(__name__)
    
    # Load configuration
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'production')
    application.config.from_object(config[config_name])
    
    # Initialize Database
    init_db(application)
    
    # Register Blueprints
    application.register_blueprint(auth_bp)
    application.register_blueprint(services_bp)
    application.register_blueprint(mgmt_bp)
    application.register_blueprint(main_bp)
    
    return application

# Create app instance for gunicorn (gunicorn app:app)
app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)