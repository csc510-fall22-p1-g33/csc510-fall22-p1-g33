from flask import Blueprint
from flask import request
from ..extensions import db
from ..models.all import User, Userabout, Project
from flask import jsonify

user = Blueprint('user', __name__)

@user.route('/', methods=['POST'])
def post_user():
    args = request.get_json()

    username = args['username']
    password = args['password']
    about = args['about']

    u = User.query.filter_by(username=username).first()
    if u is not None:
        return f'Conflict: User already exists.', 409

    u = User(username=username, password=password)
    db.session.add(u)
    db.session.commit()

    ua = Userabout(user_id=u.id, name=about['name'], email=about['email'], phone=about['phone'], bio=about['bio'])
    db.session.add(ua)
    db.session.commit()

    return jsonify({ "id": u.id }), 201

@user.route('/<id>', methods=['GET'])
def get_user_id(id):
    u = User.query.filter_by(id=id).first()
    if u is None:
        return f'Not Found', 404
    ua = Userabout.query.filter_by(user_id=u.id).first()
    ret = {
        "user": {
            "id": str(u.id),
            "username": str(u.username),
            "password": str(u.password),
            "projects": list(map(lambda p: str(p.id), u.projects)),
            "about": {
                "name": str(ua.name),
                "email": str(ua.email),
                "phone": str(ua.phone),
                "bio": str(ua.bio)
            }
        }
    }
    return jsonify(ret), 200

@user.route('/<id>', methods=['DELETE'])
def delete_user_id():
    # TODO: Implement
    return '501 Not Implemented', 501

@user.route('/<id>/about', methods=['PATCH'])
def patch_user_id_about(id):
    args = request.get_json()
    about = args['about']

    ua = Userabout.query.filter_by(user_id=id).first()
    if ua is None:
        return 'Not Found', 404

    ua.name = about['name']
    ua.email = about['email']
    ua.phone = about['phone']
    ua.bio = about['bio']

    db.session.add(ua)
    db.session.commit()
    
    return 'OK', 200