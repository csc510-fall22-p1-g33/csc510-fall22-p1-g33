from re import T
from flask import Blueprint
from flask import request
from ..extensions import db
from ..models.all import Joinrequest, User, Team
from flask import jsonify

joinrequest = Blueprint('joinrequest', __name__)

@joinrequest.route('/query', methods=['GET'])
def get_joinrequest_query():
    js = list(map(lambda j: str(j.id), Joinrequest.query.all()))
    return jsonify({'join_requests': [] + js}), 200

# TITHI
@joinrequest.route('/received', methods=['GET'])
def get_received_joinrequests():
    uid = request.args.get('user')
    tid = request.args.get('team')
    print ("user:", uid)
    print ("team:", tid)

    ret_list = []

    js = Joinrequest.query.all()
    for item in js:
        # print (item.id)
        # print (item.user)
        # print (item.team.id)
        # print (item.status)

        print ("user", uid, item.user.id)
        print ("team", tid, item.team.id)

        t = Team.query.filter_by(id=tid).first()
        if t is None:
            return f'Not Found', 404

        if str(tid) == str(item.team.id) and str(uid) != str(item.user.id):
            print ("user id", uid, "got join req for team id", tid, "from user id", item.user.id)
            u = User.query.filter_by(id=item.user.id).first()
            # for i in u.join_requests:
            #     print (i)
            ret = {
                    "join_request": {
                        "who_sent_id":  item.user.id,
                        "who_sent_uname": u.username,
                        "who_received": uid,
                        "req_id": item.id,
                        "team_id": item.team.id,
                        "status": item.status
                    }
            }
            ret_list.append (ret)
            
    return jsonify(ret_list), 200

@joinrequest.route('/', methods=['POST'])
def post_joinrequest():
    args = request.get_json()

    creator = args['creator']
    team = args['team']

    u = User.query.filter_by(id=creator).first()
    t = Team.query.filter_by(id=team).first()
    if u is None or t is None:
        return 'Not Found', 404

    # TODO: check if user is in the project that the team is in
    # TODO: check if user is already in a team in the project
    
    j = Joinrequest.query.filter_by(user_id=u.id, team_id=t.id).first()
    if j is None:
        j = Joinrequest(user_id=u.id, team_id=t.id, status='pending')
    
    if j.status != 'pending' and j.status != 'withdrawn':
        return 'Conflict', 409
    
    j.status = 'pending'

    db.session.add(j)
    db.session.commit()

    return jsonify({ "id": j.id }), 200

@joinrequest.route('/<id>', methods=['GET'])
def get_joinrequest_id(id):
    j = Joinrequest.query.filter_by(id=id).first()
    if j is None:
        return f'Not Found', 404
    ret = {
        "join_request": {
            "id": str(j.id),
            "user": str(j.user.id),
            "team": str(j.team.id),
            "status": str(j.status)
        }
    }
    return jsonify(ret), 200

@joinrequest.route('/<id>', methods=['DELETE'])
def delete_joinrequest_id(id):
    # TODO: implement
    return 'Not Implemented', 501

@joinrequest.route('/<id>/accept', methods=['PATCH'])
def patch_joinrequest_id_accept(id):
    j = Joinrequest.query.filter_by(id=id).first()
    if j is None:
        return 'Not Found', 404
    if j.status != 'pending':
        return 'Conflict', 409

    u = j.user
    t = j.team
    
    t.users.append(u)
    j.status = 'accepted'

    for uj in u.join_requests:
        if j.id != uj.id:
            uj.status = 'withdrawn'
            db.session.add(uj)

    db.session.add(t)
    db.session.add(j)

    db.session.commit()
    
    return 'OK', 200

@joinrequest.route('/<id>/reject', methods=['PATCH'])
def patch_joinrequest_id_reject(id):
    j = Joinrequest.query.filter_by(id=id).first()
    if j is None:
        return 'Not Found', 404
    if j.status != 'pending':
        return 'Conflict', 409
    
    j.status = 'rejected'

    db.session.add(j)
    db.session.commit()
    
    return 'OK', 200

@joinrequest.route('/<id>/withdraw', methods=['PATCH'])
def patch_joinrequest_id_withdraw(id):
    j = Joinrequest.query.filter_by(id=id).first()
    if j is None:
        return 'Not Found', 404
    if j.status != 'pending' and j.status != 'rejected':
        # TODO: redecide this functionality
        # No way to un-reject, so users can withdraw and reapply as a temp fix
        return 'Conflict', 409
    
    j.status = 'withdrawn'

    db.session.add(j)
    db.session.commit()
    
    return 'OK', 200