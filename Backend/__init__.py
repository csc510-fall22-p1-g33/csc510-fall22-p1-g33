from flask import Flask 
from .extensions import db, migrate
from .routes.main import main
from .models.all import User,Project
# from .routes.api import api
from .routes.register import registerer

# import flask_restless

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)


    app.register_blueprint(main)
    # app.register_blueprint(api)
    # app.register_blueprint(registerer) 
    # app.run()



    # Create the Flask-Restless API manager.
    # manager = flask_restless.APIManager(app, session=db.session)

    # Create API endpoints, which will be available at /api/<tablename> by
    # default. Allowed HTTP methods can be specified as well.
    # manager.create_api(User, methods=['GET', 'POST', 'DELETE'])
    # manager.create_api(Project, methods=['GET'])

    return app