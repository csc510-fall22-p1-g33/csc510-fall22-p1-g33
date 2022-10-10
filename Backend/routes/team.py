from flask import Blueprint
from flask import request
from ..extensions import db
from ..models.all import Team, Teamabout, Project, User, Joinrequest
from flask import jsonify
from flasgger import swag_from

team = Blueprint('team', __name__)


@team.route('/query', methods=['GET'])
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
                            "teams": {
                                "type": "array",
                                "description": "List of team ids.",
                                "items": {
                                    "type": "string"
                                }
                            }
                        },
                        "required": [
                            "teams"
                        ]
                    },
                    "examples": {
                        "example-1": {
                            "value": {
                                "teams": [
                                    "1"
                                ]
                            }
                        }
                    }
                }
            }
        }
    },
    "operationId": "get-team-query",
    "description": "Query a list of all team ids."
})
def get_team_query():
    ts = list(map(lambda t: str(t.id), Team.query.all()))
    return jsonify({'teams': [] + ts}), 200


@team.route('/', methods=['POST'])
@swag_from({
    "summary": "create team",
    "operationId": "post-team",
    "responses": {
        "201": {
            "description": "Created",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "string",
                                "description": "ID of created team."
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
                        "project": {
                            "type": "string",
                            "description": "Project id."
                        }
                    },
                    "required": [
                        "creator",
                        "project"
                    ]
                },
                "examples": {
                    "example-1": {
                        "value": {
                            "creator": "1",
                            "project": "1"
                        }
                    }
                }
            }
        },
        "description": "Team information."
    },
    "description": "Create team."
})
def post_team():
    args = request.get_json()
    creator = args['creator']
    project = args['project']

    u = User.query.filter_by(id=creator).first()
    if u is None:
        return 'Not Found', 404
    p = Project.query.filter_by(id=project).first()
    if p is None:
        return 'Not Found', 404

    t = Team(project_id=p.id, filled=False)
    db.session.add(t)
    db.session.commit()

    ta = Teamabout(team_id=t.id, name='Project Tic Tac', description='Lorem')
    db.session.add(ta)
    db.session.commit()

    t = Team.query.filter_by(id=t.id).first()
    t.users.append(u)
    j = Joinrequest(team_id=t.id, user_id=u.id, status='accepted')
    db.session.add(t)
    db.session.add(j)
    db.session.commit()

    return jsonify({"id": t.id}), 201


@team.route('/<id>', methods=['GET'])
@swag_from({
    "summary": "get team",
    "tags": [],
    "operationId": "get-team-id",
    "responses": {
        "200": {
            "description": "OK",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "team": {
                                "title": "Team",
                                "x-stoplight": {
                                    "id": "dqji9r4wcfr3e"
                                },
                                "type": "object",
                                "examples": [
                                    {
                                        "id": "1",
                                        "project": "1",
                                        "users": [
                                            "1"
                                        ],
                                        "join_requests": [
                                            "1"
                                        ],
                                        "filled": False,
                                        "about": {
                                            "name": "Team A",
                                            "description": "This is Team A."
                                        }
                                    }
                                ],
                                "description": "Team information.",
                                "properties": {
                                    "id": {
                                        "type": "string",
                                        "description": "Team id."
                                    },
                                    "project": {
                                        "type": "string",
                                        "description": "ID of project that team is for."
                                    },
                                    "users": {
                                        "type": "array",
                                        "description": "IDs of users in team.",
                                        "items": {
                                            "type": "string"
                                        }
                                    },
                                    "join_requests": {
                                        "type": "array",
                                        "description": "IDs of join requests to team.",
                                        "items": {
                                            "type": "string"
                                        }
                                    },
                                    "filled": {
                                        "type": "boolean",
                                        "description": "Whether team is filled or not."
                                    },
                                    "about": {
                                        "title": "Team.About",
                                        "x-stoplight": {
                                            "id": "0utrdm5npenjf"
                                        },
                                        "type": "object",
                                        "examples": [
                                            {
                                                "name": "Team A",
                                                "description": "This is Team A."
                                            }
                                        ],
                                        "description": "Team's about fields.",
                                        "properties": {
                                            "name": {
                                                "type": "string",
                                                "description": "Team name."
                                            },
                                            "description": {
                                                "type": "string",
                                                "description": "Team description."
                                            }
                                        },
                                        "required": [
                                            "name",
                                            "description"
                                        ]
                                    }
                                },
                                "required": [
                                    "id",
                                    "project",
                                    "users",
                                    "join_requests",
                                    "filled",
                                    "about"
                                ]
                            }
                        },
                        "required": [
                            "team"
                        ]
                    },
                    "examples": {
                        "example-1": {
                            "value": {
                                "team": {
                                    "id": "1",
                                    "project": "1",
                                    "users": [
                                        "1"
                                    ],
                                    "join_requests": [
                                        "1"
                                    ],
                                    "filled": False,
                                    "about": {
                                        "name": "Team A",
                                        "description": "This is Team A."
                                    }
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
    "description": "Get team by id."
})
def get_team_id(id):
    t = Team.query.filter_by(id=id).first()
    if t is None:
        return 'Not Found', 404

    ta = Teamabout.query.filter_by(team_id=t.id).first()
    ret = {
        "team": {
            "id": str(t.id),
            "users": list(map(lambda u: str(u.id), t.users)),
            "join_requests": list(map(lambda j: str(j.id), t.join_requests)),
            "project": str(t.project.id),
            "about": {
                "name": str(ta.name),
                "description": str(ta.description)
            }
        }
    }
    return jsonify(ret), 200


@team.route('/<id>', methods=['DELETE'])
@swag_from({
    "summary": "delete team",
    "operationId": "delete-team-id",
    "responses": {
        "200": {
            "description": "OK"
        },
        "404": {
            "description": "Not Found"
        }
    },
    "description": "Delete team by id.\n\nWARNING: Teams are now automatically deleted when all users leave them. There is no reason to use this method in normal operations.",
    "deprecated": True
})
def delete_team_id(id):
    # TODO: Remove this route and move deletion logic to user removal
    # ALERT: YOU SHOULD NOT BE CALLING THIS IN NORMAL USE
    # DELETION OCCURS WHEN LAST USER IS REMOVED, AUTOMATICALLY
    t = Team.query.filter_by(id=id).first()
    if t is None:
        return f'Not Found', 404
    db.session.delete(t)
    db.session.commit()
    return 'OK', 200

# @team.route('/<id>/users/add', methods=['PATCH'])
# def patch_project_id_users_add(id):
#     p = Project.query.filter_by(id=id).first()
#     if p is None:
#         return f'Not Found', 404
#     args = request.get_json()
#     uid = args['user_id']
#     u = User.query.filter_by(id=uid).first()
#     if u is None:
#         return f'Not Found', 404
#     p.users.append(u)
#     db.session.add(p)
#     db.session.commit()
#     return 'OK', 200


@team.route('/<id>/users/remove', methods=['PATCH'])
@swag_from({
    "summary": "remove user from team",
    "operationId": "patch-team-id-users-remove",
    "responses": {
        "200": {
            "description": "OK"
        },
        "404": {
            "description": "Not Found"
        }
    },
    "requestBody": {
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "User id."
                        }
                    },
                    "required": [
                        "user_id"
                    ]
                },
                "examples": {
                    "example-1": {
                        "value": {
                            "user_id": "1"
                        }
                    }
                }
            }
        },
        "description": ""
    },
    "description": "Remove user from team."
})
def patch_team_id_users_remove(id):
    # ALERT: THIS DELETES THE PROJECT IF NO USERS ARE LEFT.
    t = Team.query.filter_by(id=id).first()
    if t is None:
        return f'Not Found', 404
    args = request.get_json()
    uid = args['user_id']
    u = User.query.filter_by(id=uid).first()
    if u is None or u not in t.users:
        return f'Not Found', 404
    t.users.remove(u)
    j = Joinrequest.query.filter_by(team_id=t.id, user_id=u.id).first()
    j.status = 'withdrawn'
    db.session.add(t)
    db.session.add(j)
    db.session.commit()
    # TODO: redo deletion thing, looks sketchy
    t = Team.query.filter_by(id=id).first()
    if len(t.users) == 0:
        delete_team_id(id)
    return 'OK', 200


@team.route('/<id>/about', methods=['PATCH'])
@swag_from({
    "summary": "edit team about",
    "operationId": "patch-team-id-about",
    "responses": {
        "200": {
            "description": "OK"
        },
        "404": {
            "description": "Not Found"
        }
    },
    "requestBody": {
        "content": {
            "application/json": {
                "schema": {
                    "title": "Team.About",
                    "x-stoplight": {
                        "id": "0utrdm5npenjf"
                    },
                    "type": "object",
                    "examples": [
                        {
                            "name": "Team A",
                            "description": "This is Team A."
                        }
                    ],
                    "description": "Team's about fields.",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Team name."
                        },
                        "description": {
                            "type": "string",
                            "description": "Team description."
                        }
                    },
                    "required": [
                        "name",
                        "description"
                    ]
                }
            }
        },
        "description": "Team's new about fields."
    },
    "description": "Edit team's about fields."
})
def patch_team_id_about(id):
    t = Team.query.filter_by(id=id).first()
    if t is None:
        return f'Not Found', 404
    args = request.get_json()
    ta = t.about
    ta.name = args['name']
    ta.description = args['description']
    db.session.add(ta)
    db.session.commit()
    return 'OK', 200


@team.route('/<id>/filled', methods=['PATCH'])
@swag_from({
    "summary": "set team filled",
    "operationId": "patch-team-id-filled",
    "responses": {
        "200": {
            "description": "OK"
        },
        "404": {
            "description": "Not Found"
        }
    },
    "requestBody": {
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "filled": {
                            "type": "boolean",
                            "description": "Whether team is filled."
                        }
                    },
                    "required": [
                        "filled"
                    ]
                },
                "examples": {
                    "example-1": {
                        "value": {
                            "filled": True
                        }
                    }
                }
            }
        }
    },
    "description": "Set whether team is filled.\nNOT IMPLEMENTED YET."
})
def patch_team_id_filled(id):
    return 'Not Implemented', 501
