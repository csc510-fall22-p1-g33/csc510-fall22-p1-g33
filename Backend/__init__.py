from flask import Flask 
from .extensions import db, migrate

# from .models.all import User,Project
# from .routes.register import registerer

from .routes.main import main
from .routes.joinrequest import joinrequest
from .routes.project import project
from .routes.team import team
from .routes.user import user

import os

# import flask_restless

def create_app():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'db.sqlite3')

    app = Flask(__name__)
    app.url_map.strict_slashes = False
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{filename}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main, url_prefix='/')
    app.register_blueprint(joinrequest, url_prefix='/join_request/')
    app.register_blueprint(project, url_prefix='/project/')
    app.register_blueprint(team, url_prefix='/team/')
    app.register_blueprint(user, url_prefix='/user/')

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