from flask import Flask
from .extensions import db, migrate
from flasgger import Swagger
import json
# from .models.all import User,Project
# from .routes.register import registerer

from .routes.main import main
from .routes.joinrequest import joinrequest
from .routes.project import project
from .routes.team import team
from .routes.user import user
from flasgger import Swagger

import os

import os

# import flask_restless


def create_app():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'db.sqlite3')

    app = Flask(__name__)

    app.config['SWAGGER'] = {
        'openapi': '3.0.3'
    }
    s_template = {
        "info": {
            "title": "tft-backend",
            "version": "0.0.1",
            "description": "Team Formation Tool backend documentation.",
            "contact": {
                "url": "https://github.com/sreedhara-aneesh/csc510-fall22-p1-g33"
            },
            "termsOfService": "https://github.com/sreedhara-aneesh/csc510-fall22-p1-g33/blob/main/LICENSE.md"
        },
        "servers": [
            {
                "description": "Local development server.",
                "url": "http://localhost:5000"
            }
        ],
    }

    swagger = Swagger(app, template=s_template)

    app.url_map.strict_slashes = False

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{filename}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main, url_prefix='/')
    app.register_blueprint(joinrequest, url_prefix='/joinrequest/')
    app.register_blueprint(project, url_prefix='/project/')
    app.register_blueprint(team, url_prefix='/team/')
    app.register_blueprint(user, url_prefix='/user/')

    with app.app_context():
        specgen = json.dumps(swagger.get_apispecs())
        specgenfile = open(os.path.join(
            os.path.dirname(__file__), 'docs/specgen.json'), 'w')
        specgenfile.write(specgen)
        specgenfile.close()

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
