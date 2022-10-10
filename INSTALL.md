# Installation and quick start instructions



# Backend

## Development environment prerequisites
This application needs 
- Flask 1.1.2 or above
- Python 3.8 or above
- pytest 7.1.1 or above

 To download the external library dependencies for python, run the following command in the project root directory:

```console
pip install -r requirements.txt
```

## Installation

1. Create virtual environment 
    
        python3 -m venv venv 

1. Activate the virtual environment 

    Windows:

        venv\Scripts\activate 
    
    Linux/Mac:

        source venv/bin/activate

1. Install dependencies and set environment 
        
        pip install -r Backend/requirements.txt
        
1. Set environment variables
    
    Windows:

        SET FLASK_APP=Backend
        SET FLASK_DEBUG=1
        
    Linux/Mac:

        export FLASK_APP=Backend
        export FLASK_DEBUG=1

1. Remove old files if any  
        
        rm instance/db.sqlite3
        rm -r migrations
        
1. Create new db
    
        flask db init 
        flask db migrate
        flask db upgrade

1. Run the backend
        
        flask run

## Or Run in Docker 

1. You can run our backend in a docker container by running the following commands
        
        sudo docker build -t backend -f backend.Dockerfile .
        sudo docker run --name backend --rm -d -p 5000:5000 -t backend
# Frontend

## Development environment prerequisites

- Make sure you have a recent version of [Node.js](https://nodejs.org/en/) installed.

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.
## Documentation 
1. [Flask](https://flask.palletsprojects.com/en/2.2.x/)
1. [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/)
1. [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
