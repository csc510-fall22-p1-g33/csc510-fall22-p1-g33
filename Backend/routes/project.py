from flask import Blueprint
from flask import request
from ..extensions import db
from ..models.all import Project, Projectabout, User
from flask import jsonify
from flasgger import swag_from

project = Blueprint('project', __name__)

@project.route('/query', methods=['GET'])
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
                            "projects": {
                                "type": "array",
                                "description": "List of project ids.",
                                "items": {
                                    "type": "string"
                                }
                            }
                        },
                        "required": [
                            "projects"
                        ]
                    },
                    "examples": {
                        "example-1": {
                            "value": {
                                "projects": [
                                    "1"
                                ]
                            }
                        }
                    }
                }
            }
        }
    },
    "operationId": "get-project-query",
    "description": "Query a list of all project ids."
})
def get_project_query():
    ps = list(map(lambda p: str(p.id), Project.query.all()))
    return jsonify({'projects': [] + ps}), 200


@project.route('/', methods=['POST'])
@swag_from({
    "summary": "create project",
    "operationId": "post-project",
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
                                "description": "ID of created project."
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
                        }
                    },
                    "required": [
                        "creator"
                    ]
                },
                "examples": {
                    "example-1": {
                        "value": {
                            "creator": "1"
                        }
                    }
                }
            }
        },
        "description": ""
    },
    "description": "Create project."
})
def post_project():
    print (request)
    args = request.get_json()
    creator = args['creator']
    project_name = args['name']
    project_desc = args['description']

    print ("POST Project:", creator, project_name, project_desc)

    u = User.query.filter_by(id=creator).first()
    if u is None:
        return 'Not Found', 404

    p = Project()
    db.session.add(p)
    db.session.commit()
    
    pa = Projectabout(project_id=p.id, name=project_name, description=project_desc)
    db.session.add(pa)
    db.session.commit()

    p = Project.query.filter_by(id=p.id).first()
    p.users.append(u)
    db.session.add(p)
    db.session.commit()

    return jsonify({ "id": p.id }), 201

@project.route('/<id>', methods=['GET'])
@swag_from({
    "summary": "get project",
    "tags": [],
    "responses": {
        "200": {
            "description": "OK",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "project": {
                                "title": "Project",
                                "x-stoplight": {
                                    "id": "0xlfekcs0zwju"
                                },
                                "type": "object",
                                "examples": [
                                    {
                                        "id": "1",
                                        "teams": [
                                            "1"
                                        ],
                                        "users": [
                                            "1"
                                        ],
                                        "about": {
                                            "name": "Project A",
                                            "description": "This is project A."
                                        }
                                    }
                                ],
                                "description": "Project information.",
                                "properties": {
                                    "id": {
                                        "type": "string",
                                        "description": "Project id."
                                    },
                                    "teams": {
                                        "type": "array",
                                        "description": "IDs of teams in project.",
                                        "items": {
                                            "type": "string"
                                        }
                                    },
                                    "users": {
                                        "type": "array",
                                        "description": "IDs of users in project.",
                                        "items": {
                                            "type": "string"
                                        }
                                    },
                                    "about": {
                                        "title": "Project.About",
                                        "x-stoplight": {
                                            "id": "4xultd4qlc994"
                                        },
                                        "type": "object",
                                        "examples": [
                                            {
                                                "name": "Project A",
                                                "description": "This is project A."
                                            }
                                        ],
                                        "description": "Project's about fields.",
                                        "properties": {
                                            "name": {
                                                "type": "string",
                                                "description": "Project name."
                                            },
                                            "description": {
                                                "type": "string",
                                                "description": "Project description."
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
                                    "teams",
                                    "users",
                                    "about"
                                ]
                            }
                        },
                        "required": [
                            "project"
                        ]
                    },
                    "examples": {
                        "example-1": {
                            "value": {
                                "project": {
                                    "id": "1",
                                    "teams": [
                                        "1"
                                    ],
                                    "users": [
                                        "1"
                                    ],
                                    "about": {
                                        "name": "Project A",
                                        "description": "This is project A."
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
    "operationId": "get-project-id",
    "description": "Get project by id."
})
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
@swag_from({
    "summary": "delete project",
    "operationId": "delete-project-id",
    "responses": {
        "200": {
            "description": "OK"
        },
        "404": {
            "description": "Not Found"
        }
    },
    "description": "Delete project by id.\n\nWARNING: Projects are now deleted automatically when all users leave them. There is no reason to use this method in normal operations.",
    "deprecated": True
})
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
@swag_from({
    "summary": "add user to project",
    "operationId": "patch-project-id-users-add",
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
    "description": "Add user to project."
})
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
@swag_from({
    "summary": "remove user from project",
    "operationId": "patch-project-id-users-remove",
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
        }
    },
    "description": "Remove user from project."
})
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
@swag_from({
    "summary": "edit project about",
    "operationId": "patch-project-id-about",
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
                    "title": "Project.About",
                    "x-stoplight": {
                        "id": "4xultd4qlc994"
                    },
                    "type": "object",
                    "examples": [
                        {
                            "name": "Project A",
                            "description": "This is project A."
                        }
                    ],
                    "description": "Project's about fields.",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Project name."
                        },
                        "description": {
                            "type": "string",
                            "description": "Project description."
                        }
                    },
                    "required": [
                        "name",
                        "description"
                    ]
                },
                "examples": {
                    "example-1": {
                        "value": {
                            "name": "Project A",
                            "description": "This is project A."
                        }
                    }
                }
            }
        },
        "description": "Project's new about fields."
    },
    "description": "Edit project's about fields."
})
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