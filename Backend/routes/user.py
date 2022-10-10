from flask import Blueprint
from flask import request
from ..extensions import db
from ..models.all import User, Userabout, Project, Projectabout
from flask import jsonify
import re
from flasgger import swag_from

user = Blueprint('user', __name__)

# TITHI


@user.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    u = User.query.filter_by(username=username).first()
    if u is None:
        return 'Not Found', 200
    searched_id = u.id
    u = User.query.filter_by(id=searched_id).first()
    if u is None:
        return f'Not Found', 404
    ua = Userabout.query.filter_by(user_id=u.id).first()

    ret_success = {
        "user_id": searched_id,
        "login": "SUCCESS"
    }
    ret_failed = {
        "user_id": searched_id,
        "login": "FAIL"
    }

    if u.password == password:
        return jsonify(ret_success), 200
    else:
        return jsonify(ret_failed), 400

# TITHI


@user.route('/querybyusername', methods=['GET'])
def get_user_query():
    username = request.args.get('username')

    u = User.query.filter_by(username=username).first()
    if u is None:
        return 'Not Found', 200
    print(u.projects[0].id)
    return jsonify({'user': str(u.id)}), 200


# TITHI
@user.route('/firstproject', methods=['GET'])
def get_user_first_projectid():
    user_id = request.args.get('user_id')

    u = User.query.filter_by(id=user_id).first()
    if u is None:
        return 'Not Found', 200
    # print (u.projects[0].id)
    if (len(u.projects) == 0):
        pid = -1
        ret = {
            "project": {
                "id": -1
            }
        }
    else:
        pid = str(u.projects[0].id)

        pa = Projectabout.query.filter_by(project_id=pid).first()
        ret = {
            "project": {
                "id": str(pid),
                "users": list(map(lambda u: str(u.id), u.projects[0].users)),
                "teams": list(map(lambda t: str(t.id), u.projects[0].teams)),
                "about": {
                    "name": str(pa.name),
                    "description": str(pa.description)
                }
            }
        }

    return jsonify({'first_pid': pid, "first_project": ret}), 200

# TITHI


@user.route('/reg', methods=['POST'])
def reg_user():
    args = request.get_json()

    username = args['username']
    password = args['password']
    about = args['about']

    if username == "":
        return jsonify({"id": -1, "error_type": "Username is required."}), 400
    elif password == "":
        return jsonify({"id": -1, "error_type": "Password is required."}), 400
    elif not re.match(r'[^@]+@[^@]+\.[^@]+', about['email']):
        return jsonify({"id": -1, "error_type": "Invalid email address!"}), 400

    u = User.query.filter_by(username=username).first()
    if u is not None:
        return jsonify({"id": -1, "error_type": "Conflict: User already exists."}), 400

    u = User(username=username, password=password)
    db.session.add(u)
    db.session.commit()

    ua = Userabout(
        user_id=u.id, name=about['name'], email=about['email'], phone=about['phone'], bio=about['bio'])
    db.session.add(ua)
    db.session.commit()

    return jsonify({"id": u.id, "error_type": "No Error!"}), 201


@user.route('/query', methods=['GET'])
@swag_from({
    "summary": "Your GET endpoint",
    "tags": [],
    "responses": {
        "200": {
            "description": "OK",
            "headers": {},
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "user": {
                                "type": "string",
                                "description": "User id."
                            }
                        },
                        "required": [
                            "user"
                        ]
                    },
                    "examples": {
                        "example-1": {
                            "value": {
                                "user": "1"
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
    "operationId": "get-user-query",
    "requestBody": {
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "username": {
                            "type": "string",
                            "description": "User username."
                        }
                    },
                    "required": [
                        "username"
                    ]
                },
                "examples": {
                    "example-1": {
                        "value": {
                            "username": "jdoe"
                        }
                    }
                }
            }
        }
    },
    "description": "Query for user id by username."
})
def get_team_query():
    args = request.get_json()
    username = args['username']
    u = User.query.filter_by(username=username).first()
    if u is None:
        return 'Not Found', 200
    return jsonify({'user': str(u.id)}), 200


@user.route('/', methods=['POST'])
@swag_from({
    "summary": "create user",
    "operationId": "post-user",
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
                                "description": "ID of created user."
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
        "409": {
            "description": "Conflict: User already exists."
        }
    },
    "requestBody": {
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "username": {
                            "type": "string",
                            "description": "User username."
                        },
                        "password": {
                            "type": "string",
                            "description": "User password."
                        },
                        "about": {
                            "description": "User's about fields.",
                            "title": "User.About",
                            "x-stoplight": {
                                "id": "j1en02su7pbr7"
                            },
                            "type": "object",
                            "examples": [
                                {
                                    "name": "John Doe",
                                    "email": "jdoe@ncsu.edu",
                                    "phone": "9999999999",
                                    "bio": "I am cool."
                                }
                            ],
                            "properties": {
                                "name": {
                                    "type": "string",
                                    "description": "User name."
                                },
                                "email": {
                                    "type": "string",
                                    "description": "User email."
                                },
                                "phone": {
                                    "type": "string",
                                    "description": "User phone."
                                },
                                "bio": {
                                    "type": "string",
                                    "description": "User bio."
                                }
                            },
                            "required": [
                                "name",
                                "email",
                                "phone",
                                "bio"
                            ]
                        }
                    },
                    "required": [
                        "username",
                        "password",
                        "about"
                    ]
                },
                "examples": {
                    "example-1": {
                        "value": {
                            "username": "jdoe",
                            "password": "abc123",
                            "about": {
                                "name": "John Doe",
                                "email": "jdoe@ncsu.edu",
                                "phone": "9999999999",
                                "bio": "I am cool."
                            }
                        }
                    }
                }
            }
        },
        "description": "User information."
    },
    "description": "Create user."
})
def post_user():
    args = None

    try:
        args = request.get_json()
    except:
        print("An exception occurred")

    username = args['username']
    password = args['password']
    about = args['about']

    u = User.query.filter_by(username=username).first()
    if u is not None:
        return f'Conflict: User already exists.', 409

    u = User(username=username, password=password)
    db.session.add(u)
    db.session.commit()

    ua = Userabout(
        user_id=u.id, name=about['name'], email=about['email'], phone=about['phone'], bio=about['bio'])
    db.session.add(ua)
    db.session.commit()

    return jsonify({"id": u.id}), 201


@user.route('/<id>', methods=['GET'])
@swag_from({
    "summary": "get user",
    "tags": [],
    "responses": {
        "200": {
            "description": "OK",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "user": {
                                "title": "User",
                                "x-stoplight": {
                                    "id": "9x0uztk59btoh"
                                },
                                "type": "object",
                                "examples": [
                                    {
                                        "id": "1",
                                        "username": "jdoe",
                                        "password": "abc123",
                                        "teams": [
                                            "1"
                                        ],
                                        "projects": [
                                            "1"
                                        ],
                                        "join_requests": [
                                            "1"
                                        ],
                                        "about": {
                                            "name": "John Doe",
                                            "email": "jdoe@ncsu.edu",
                                            "phone": "9999999999",
                                            "bio": "I am cool."
                                        }
                                    }
                                ],
                                "description": "User information.",
                                "properties": {
                                    "id": {
                                        "type": "string",
                                        "description": "User id."
                                    },
                                    "username": {
                                        "type": "string",
                                        "description": "User username."
                                    },
                                    "password": {
                                        "type": "string",
                                        "description": "User password."
                                    },
                                    "teams": {
                                        "type": "array",
                                        "description": "IDs of teams that user is in.",
                                        "items": {
                                            "type": "string"
                                        }
                                    },
                                    "projects": {
                                        "type": "array",
                                        "description": "IDs of projects that user is in.",
                                        "items": {
                                            "type": "string"
                                        }
                                    },
                                    "join_requests": {
                                        "type": "array",
                                        "description": "IDs of join requests created by the user.",
                                        "items": {
                                            "type": "string"
                                        }
                                    },
                                    "about": {
                                        "title": "User.About",
                                        "x-stoplight": {
                                            "id": "j1en02su7pbr7"
                                        },
                                        "type": "object",
                                        "examples": [
                                            {
                                                "name": "John Doe",
                                                "email": "jdoe@ncsu.edu",
                                                "phone": "9999999999",
                                                "bio": "I am cool."
                                            }
                                        ],
                                        "description": "User's about fields.",
                                        "properties": {
                                            "name": {
                                                "type": "string",
                                                "description": "User name."
                                            },
                                            "email": {
                                                "type": "string",
                                                "description": "User email."
                                            },
                                            "phone": {
                                                "type": "string",
                                                "description": "User phone."
                                            },
                                            "bio": {
                                                "type": "string",
                                                "description": "User bio."
                                            }
                                        },
                                        "required": [
                                            "name",
                                            "email",
                                            "phone",
                                            "bio"
                                        ]
                                    }
                                },
                                "required": [
                                    "id",
                                    "username",
                                    "password",
                                    "teams",
                                    "projects",
                                    "join_requests",
                                    "about"
                                ]
                            }
                        },
                        "required": [
                            "user"
                        ]
                    },
                    "examples": {
                        "example-1": {
                            "value": {
                                "user": {
                                    "id": "1",
                                    "username": "jdoe",
                                    "password": "abc123",
                                    "teams": [
                                        "1"
                                    ],
                                    "projects": [
                                        "1"
                                    ],
                                    "join_requests": [
                                        "1"
                                    ],
                                    "about": {
                                        "name": "John Doe",
                                        "email": "jdoe@ncsu.edu",
                                        "phone": "9999999999",
                                        "bio": "I am cool."
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
    "operationId": "get-user-id",
    "description": "Get user by id."
})
def get_user_id(id):
    u = User.query.filter_by(id=id).first()
    if u is None:
        return f'Not Found', 404
    ua = Userabout.query.filter_by(user_id=u.id).first()
    # CHECK
    # "join_requests": list(map(lambda p: str(p.id), u.join_requests)),
    ret = {
        "user": {
            "id": str(u.id),
            "username": str(u.username),
            "password": str(u.password),
            "projects": list(map(lambda p: str(p.id), u.projects)),
            "teams": list(map(lambda p: str(p.id), u.teams)),
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
@swag_from({
    "summary": "delete user",
    "operationId": "delete-user-id",
    "responses": {
        "200": {
            "description": "OK"
        }
    },
    "description": "Delete user by id.\nNOT YET IMPLEMENTED."
})
def delete_user_id():
    # TODO: Implement
    return '501 Not Implemented', 501


@user.route('/<id>/about', methods=['PATCH'])
@swag_from({
    "summary": "edit user about",
    "operationId": "patch-user-id-about",
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
                    "title": "User.About",
                    "x-stoplight": {
                        "id": "j1en02su7pbr7"
                    },
                    "type": "object",
                    "examples": [
                        {
                            "name": "John Doe",
                            "email": "jdoe@ncsu.edu",
                            "phone": "9999999999",
                            "bio": "I am cool."
                        }
                    ],
                    "description": "User's about fields.",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "User name."
                        },
                        "email": {
                            "type": "string",
                            "description": "User email."
                        },
                        "phone": {
                            "type": "string",
                            "description": "User phone."
                        },
                        "bio": {
                            "type": "string",
                            "description": "User bio."
                        }
                    },
                    "required": [
                        "name",
                        "email",
                        "phone",
                        "bio"
                    ]
                },
                "examples": {
                    "example-1": {
                        "value": {
                            "name": "John Doe",
                            "email": "jdoe@ncsu.edu",
                            "phone": "9999999999",
                            "bio": "I am cool."
                        }
                    }
                }
            }
        },
        "description": "User's new about fields."
    },
    "description": "Edit user's about fields by id."
})
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
