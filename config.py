import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'premium_salon_secret_key')
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/SalonAdmin')
    
class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/SalonAdmin')

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    # Use environment variable or fallback to Atlas connection
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb+srv://carlestonmashaba_db_user:x2gpdZA0Qg9d61er@cluster0.jlvmrfg.mongodb.net/SalonAdmin?retryWrites=true&w=majority')
    
class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    MONGO_URI = 'mongodb://localhost:27017/SalonAdmin_Test'

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
