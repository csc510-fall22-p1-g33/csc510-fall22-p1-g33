# Installation 

1. `python3 -m venv venv`
2. `source venv/bin/activate `
3. `venv\Scripts\activate`
4. `pip install -r Backend/requirements.txt`
5. `export FLASK_APP=Backend`
6. `export FLASK_DEBUG=1`
7. `rm Backend/db.sqlite3`
7. `flask db init`
8. `flask db migrate`
9. `flask db upgrade`
10. `flask run`

# To check sqlite db
- `sqlite3 Backend/db.sqlite3`
- `select * from user;`
- `.exit`
- `.tables`
- `.schema`

# Fill up db
- `insert into Userabout values (1,'ljk', 232,'kljadkfj', '12-12-12', '11-11-11', 1);`

# TODO 
- Use [flasgger](https://github.com/flasgger/flasgger) to add swagger documentation for backend 
- Use [flask validator](https://flask-validator.readthedocs.io/en/latest/) to validate fields 
- Method for adding CRUD Rest API and Swagger documentation - https://www.imaginarycloud.com/blog/flask-python/ 


<!-- 
4. `pip install flask `
4. `pip install -U Flask-SQLAlchemy`
4. `pip install Flask-Migrate` -->