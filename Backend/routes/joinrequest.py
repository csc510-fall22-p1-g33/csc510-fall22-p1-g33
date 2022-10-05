from flask import Blueprint

joinrequest = Blueprint('joinrequest', __name__)

@joinrequest.route('/')
def index():
    return "Hello world!"