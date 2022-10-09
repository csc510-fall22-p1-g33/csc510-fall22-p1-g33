from flask import Blueprint

from ..extensions import db
from ..models.all import User
# from ..models.user import User
# from ..models.team import Team
# from ..models.project import Project

from flasgger.utils import swag_from
 

main = Blueprint('main', __name__)

@swag_from("./docs/main_api_doc.yml")
@main.route('/')
def index():
    print ("here")
    return "Hello world!"


# @main.route('/user/<name>')
# def create_user(name):
#     user = User(username=name, password="12345",email=name+"jnj@gmaj.vom")
#     db.session.add(user)
#     db.session.commit()
#     return 'Created User!'