from re import T
from flask import Blueprint
from flask import request
from ..extensions import db
from ..models.all import Joinrequest, User, Team
from flask import jsonify
from flasgger import swag_from

joinrequest = Blueprint('joinrequest', __name__)


@joinrequest.route('/query', methods=['GET'])
@swag_from({
    "summary": "Your GET endpoint",
    "tags": [],
    "responses": {
        "200": {
            "description": "OK",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "join_requests": {
                                "type": "array",
                                "description": "List of join request ids.",
                                "items": {
                                    "type": "string"
                                }
                            }
                        },
                        "required": [
                            "join_requests"
                        ]
                    },
                    "examples": {
                        "example-1": {
                            "value": {
                                "join_requests": [
                                    "1"
                                ]
                            }
                        }
                    }
                }
            }
        }
    },
    "operationId": "get-join_request-query",
    "description": "Query a list of all join request ids."
})
def get_joinrequest_query():
    js = list(map(lambda j: str(j.id), Joinrequest.query.all()))
    return jsonify({'join_requests': [] + js}), 200

# TITHI


@joinrequest.route('/received', methods=['GET'])
def get_received_joinrequests():
    uid = request.args.get('user')
    tid = request.args.get('team')
    print("user:", uid)
    print("team:", tid)

    ret_list = []

    js = Joinrequest.query.all()
    for item in js:
        # print (item.id)
        # print (item.user)
        # print (item.team.id)
        # print (item.status)

        print("user", uid, item.user.id)
        print("team", tid, item.team.id)

        t = Team.query.filter_by(id=tid).first()
        if t is None:
            return f'Not Found', 404

        if str(tid) == str(item.team.id) and str(uid) != str(item.user.id):
            print("user id", uid, "got join req for team id",
                  tid, "from user id", item.user.id)
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
            ret_list.append(ret)

    return jsonify(ret_list), 200


@joinrequest.route('/', methods=['POST'])
@swag_from({
    "summary": "create join request",
    "operationId": "post-join_request",
    "responses": {
        "200": {
            "description": "OK",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "string",
                                "description": "ID of created join request."
                            }
                        },
                        "required": [
                            "id"
                        ]
                    },
                    "examples": {
                        "example-1": {
                            "value": {
                                "id": "1"
                            }
                        }
                    }
                }
            }
        },
        "404": {
            "description": "Not Found"
        },
        "409": {
            "description": "Conflict"
        }
    },
    "requestBody": {
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "creator": {
                            "type": "string",
                            "description": "Creator user id."
                        },
                        "team": {
                            "type": "string",
                            "description": "Team id."
                        }
                    },
                    "required": [
                        "creator",
                        "team"
                    ]
                },
                "examples": {
                    "example-1": {
                        "value": {
                            "creator": "1",
                            "team": "1"
                        }
                    }
                }
            }
        },
        "description": "Join request information."
    },
    "description": "Create join request."
})
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

    return jsonify({"id": j.id}), 200


@joinrequest.route('/<id>', methods=['GET'])
@swag_from({
    "summary": "get join request",
    "tags": [],
    "responses": {
        "200": {
            "description": "OK",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "join_request": {
                                "title": "JoinRequest",
                                "x-stoplight": {
                                    "id": "9g1dzsnj5m2aa"
                                },
                                "type": "object",
                                "examples": [
                                    {
                                        "id": "1",
                                        "user": "1",
                                        "team": "1",
                                        "status": "pending"
                                    }
                                ],
                                "description": "Join request information.",
                                "properties": {
                                    "id": {
                                        "type": "string",
                                        "description": "Join request id."
                                    },
                                    "user": {
                                        "type": "string",
                                        "description": "ID of user who created join request."
                                    },
                                    "team": {
                                        "type": "string",
                                        "description": "ID of team that join request is for."
                                    },
                                    "status": {
                                        "type": "string",
                                        "enum": [
                                            "pending",
                                            "denied",
                                            "accepted",
                                            "withdrawn"
                                        ],
                                        "description": "Status of join request."
                                    }
                                },
                                "required": [
                                    "id",
                                    "user",
                                    "team",
                                    "status"
                                ]
                            }
                        },
                        "required": [
                            "join_request"
                        ]
                    },
                    "examples": {
                        "example-1": {
                            "value": {
                                "join_request": {
                                    "id": "1",
                                    "user": "1",
                                    "team": "1",
                                    "status": "pending"
                                }
                            }
                        }
                    }
                }
            }
        },
        "404": {
            "description": "Not Found"
        }
    },
    "operationId": "get-join_request-id",
    "description": "Get join request by id."
})
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
@swag_from({
    "summary": "delete join request",
    "operationId": "delete-join_request-id",
    "responses": {
        "200": {
            "description": "OK"
        }
    },
    "description": "Delete join request by id.\n\nWARNING: Join requests are now automatically deleted when their associated team or user is deleted. There is no reason to use this method in normal operations.",
    "deprecated": True
})
def delete_joinrequest_id(id):
    # TODO: implement
    return 'Not Implemented', 501


@joinrequest.route('/<id>/accept', methods=['PATCH'])
@swag_from({
    "summary": "accept join request",
    "operationId": "patch-join_request-id-accept",
    "responses": {
        "200": {
            "description": "OK"
        },
        "404": {
            "description": "Not Found"
        },
        "409": {
            "description": "Conflict"
        }
    },
    "description": "Accept join request"
})
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
@swag_from({
    "summary": "reject join request",
    "operationId": "patch-join_request-id-reject",
    "responses": {
        "200": {
            "description": "OK"
        },
        "404": {
            "description": "Not Found"
        },
        "409": {
            "description": "Conflict"
        }
    },
    "description": "Reject join request."
})
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
@swag_from({
    "summary": "withdraw join request",
    "operationId": "patch-join_request-id-withdraw",
    "responses": {
        "200": {
            "description": "OK"
        },
        "404": {
            "description": "Not Found"
        },
        "409": {
            "description": "Conflict"
        }
    },
    "description": "Withdraw join request."
})
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
