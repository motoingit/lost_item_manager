class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'moto-x' # os.random
    SQLALCHEMY_DATABASE_URI = 'sqlite:///lost_item.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DB_NAME = "lost_item.db"
    # DB_PATH = os.path.join(basedir, DB_NAME)
    DB_USERNAME = "root"
    DB_PASSWORD = "moto"
    DB_HOST = "localhost"
    DB_PORT = "3306"
    SQLALCHEMY_BINDS = {
        'log': 'sqlite:///log.db'
    }
    SESSION_COOKIE_SECURE = True
    # CSRF_ENABLED = True

class ProductionConfig(Config):
    DB_USERNAME = "2"
    DB_PASSWORD = "m2"
    DB_HOST = "localhost"
    DB_PORT = "3306"
    DEBUG = False

class DevelopmentConfig(Config):
    pass
    # DEBUG = True

class TestingConfig(Config):
    TESTING = True