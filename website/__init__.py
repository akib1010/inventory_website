from flask import Flask

def create_app():
    #initialize the flask
    app=Flask(__name__)
    #initialize the secret key
    app.config['SECRET_KEY']='very_very_secret_(shush)'

    from .views import views
    from .auth import auth
    #register the blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')

    return app



