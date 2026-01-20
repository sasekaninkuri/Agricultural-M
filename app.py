from flask import Flask
from models.database import init_db
from routes.auth import auth_bp
from routes.services import services_bp
from routes.management import mgmt_bp
from routes.main import main_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = "premium_salon_secret_key"
    
    # Initialize Database
    init_db(app)
    
    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(services_bp)
    app.register_blueprint(mgmt_bp)
    app.register_blueprint(main_bp)
    
    return app

if __name__ == "__main__":
    import os
    app = create_app()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)