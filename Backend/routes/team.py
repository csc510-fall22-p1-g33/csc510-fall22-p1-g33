from flask import Blueprint

team = Blueprint('team', __name__)

@team.route('/')
def index():
    return "Hello world!"