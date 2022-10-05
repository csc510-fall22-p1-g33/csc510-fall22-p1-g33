from flask import Blueprint
from flask import request
from ..extensions import db
from ..models.all import Project, Projectabout, User
from flask import jsonify

project = Blueprint('project', __name__)

@project.route('/', methods=['POST'])
def post_project():
    args = request.get_json()
    creator = args['creator']

    u = User.query.filter_by(id=creator).first()
    if u is None:
        return 'Not Found', 404

    p = Project()
    db.session.add(p)
    db.session.commit()
    
    pa = Projectabout(project_id=p.id, name=f'Unnamed Project', description="No description.")
    db.session.add(pa)
    db.session.commit()

    p = Project.query.filter_by(id=p.id).first()
    p.users.append(u)
    db.session.add(p)
    db.session.commit()

    return jsonify({ "id": p.id }), 201

@project.route('/<id>', methods=['GET'])
def get_project_id(id):
    p = Project.query.filter_by(id=id).first()
    if p is None:
        return f'Not Found', 404
    pa = Projectabout.query.filter_by(project_id=p.id).first()
    ret = {
        "project": {
            "id": str(p.id),
            "users": list(map(lambda u: str(u.id), p.users)),
            "teams": list(map(lambda t: str(t.id), p.teams)),
            "about": {
                "name": str(pa.name),
                "description": str(pa.description)
            }
        }
    }
    return jsonify(ret), 200

@project.route('/<id>', methods=['DELETE'])
def delete_project_id(id):
    # TODO: Remove this route and move deletion logic to user removal
    # ALERT: YOU SHOULD NOT BE CALLING THIS IN NORMAL USE
    # DELETION OCCURS WHEN LAST USER IS REMOVED, AUTOMATICALLY
    p = Project.query.filter_by(id=id).first()
    if p is None:
        return f'Not Found', 404
    db.session.delete(p)
    db.session.commit()
    return 'OK', 200

@project.route('/<id>/users/add', methods=['PATCH'])
def patch_project_id_users_add(id):
    p = Project.query.filter_by(id=id).first()
    if p is None:
        return f'Not Found', 404
    args = request.get_json()
    uid = args['user_id']
    u = User.query.filter_by(id=uid).first()
    if u is None:
        return f'Not Found', 404
    p.users.append(u)
    db.session.add(p)
    db.session.commit()
    return 'OK', 200

@project.route('/<id>/users/remove', methods=['PATCH'])
def patch_project_id_users_remove(id):
    # ALERT: THIS DELETES THE PROJECT IF NO USERS ARE LEFT.
    p = Project.query.filter_by(id=id).first()
    if p is None:
        return f'Not Found', 404
    args = request.get_json()
    uid = args['user_id']
    u = User.query.filter_by(id=uid).first()
    if u is None or u not in p.users:
        return f'Not Found', 404
    p.users.remove(u)
    db.session.add(p)
    db.session.commit()
    # TODO: redo deletion thing, looks sketchy
    p = Project.query.filter_by(id=id).first()
    if len(p.users) == 0:
        delete_project_id(id)
    return 'OK', 200

@project.route('/<id>/about', methods=['PATCH'])
def patch_project_id_about(id):
    p = Project.query.filter_by(id=id).first()
    if p is None:
        return f'Not Found', 404
    args = request.get_json()
    pa = p.about
    pa.name = args['name']
    pa.description = args['description']
    db.session.add(pa)
    db.session.commit()
    return 'OK', 200