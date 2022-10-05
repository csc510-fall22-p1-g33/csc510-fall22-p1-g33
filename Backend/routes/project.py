from flask import Blueprint

project = Blueprint('project', __name__)

@project.route('/')
def index():
    return "Hello world!"