# Team formation tool backend
## Installation 

1. Create virtual environment 
    
        python3 -m venv venv 
        source venv/bin/activate
        venv\Scripts\activate 
1. Install dependencies and set environment 
        
        pip install -r Backend/requirements.txt
        export FLASK_APP=Backend
        export FLASK_DEBUG=1

1. Remove old files if any and create new db 
        
        rm Backend/instance/db.sqlite3
        flask db init 
        flask db migrate
        flask db upgrade

1. Run the backend
        
        flask run

## TODO 
- Use [flasgger](https://github.com/flasgger/flasgger) to add swagger documentation for backend 
- Use [flask validator](https://flask-validator.readthedocs.io/en/latest/) to validate fields 
- Method for adding CRUD Rest API and Swagger documentation - https://www.imaginarycloud.com/blog/flask-python/ 

## Documentation
1. [Flask](https://flask.palletsprojects.com/en/2.2.x/)
1. [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/)
1. [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
## Commands to check sqlite db
- `sqlite3 Backend/db.sqlite3`
- `select * from user;`
- `.exit`
- `.tables`
- `.schema`



## New 
1. pip install Flask-Restless-NG 
----
<!-- DEV scratch space -->
<!-- 
4. `pip install flask `
4. `pip install -U Flask-SQLAlchemy`
4. `pip install Flask-Migrate` -->

<!-- # Fill up db
- `insert into Userabout values (1,'ljk', 232,'kljadkfj', '12-12-12', '11-11-11', 1);` -->
