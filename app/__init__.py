from flask import Flask, current_app
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config
from flask_admin import Admin

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
admin = Admin()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    with app.app_context():

        app.config['SECRET_KEY'] = 'UBSGz3-jt4GuSvF32nSbhQe-GQFkHG7oK4ZpbVY7pm4'
        app.config.from_object(config[config_name])
        config[config_name].init_app(app)

        bootstrap.init_app(app)
        mail.init_app(app)
        moment.init_app(app)
        db.init_app(app)
        login_manager.init_app(app)
        admin.init_app(app)

        from .auth import auth as auth_blueprint
        app.register_blueprint(auth_blueprint, url_prefix='/auth')

        # from .admin import admin as admin_bp
        # app.register_blueprint(admin_bp)



        from .main import main as main_blueprint
        app.register_blueprint(main_blueprint)

        from .order import order as order_blueprint
        app.register_blueprint(order_blueprint, url_prefix='/order')


        '''
        from .auth import auth as auth_blueprint
        app.register_blueprint(auth_blueprint, url_prefix='/auth')
    
        from .order import order as order_blueprint
        app.register_blueprint(order_blueprint, url_prefix='/order')
    
        from .admin import bp as admin_bp
        app.register_blueprint(admin_bp)
        '''
    return app
