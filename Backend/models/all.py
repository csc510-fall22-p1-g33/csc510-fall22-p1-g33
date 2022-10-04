from ..extensions import db

from sqlalchemy.dialects.mysql import ENUM



user_project = db.Table('user_project',
            db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
            db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True))

user_team = db.Table('user_team',
            db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
            db.Column('team_id', db.Integer, db.ForeignKey('team.id'), primary_key=True))

userabout_projects = db.Table('userabout_projects',
            db.Column('about_id', db.Integer, db.ForeignKey('userabout.id'), primary_key=True),
            db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True))

userabout_team = db.Table('userabout_team',
            db.Column('about_id', db.Integer, db.ForeignKey('userabout.id'), primary_key=True),
            db.Column('teadm_id', db.Integer, db.ForeignKey('team.id'), primary_key=True))

user_about = db.Table('user_about',
            db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
            db.Column('about_id', db.Integer, db.ForeignKey('userabout.id'), primary_key=True))

project_about = db.Table('project_about',
            db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True),
            db.Column('about_id', db.Integer, db.ForeignKey('projectabout.id'), primary_key=True))

team_about = db.Table('team_about',
            db.Column('team_id', db.Integer, db.ForeignKey('team.id'), primary_key=True),
            db.Column('about_id', db.Integer, db.ForeignKey('teamabout.id'), primary_key=True))

project_team = db.Table('project_team',
            db.Column('team_id', db.Integer, db.ForeignKey('team.id'), primary_key=True),
            db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True))

join_team = db.Table('join_team',
            db.Column('join_id', db.Integer, db.ForeignKey('joinrequest.id'), primary_key=True),
            db.Column('team_id', db.Integer, db.ForeignKey('team.id'), primary_key=True))

team_join = db.Table('team_join',
            db.Column('join_id', db.Integer, db.ForeignKey('joinrequest.id'), primary_key=True),
            db.Column('team_id', db.Integer, db.ForeignKey('team.id'), primary_key=True))

join_user = db.Table('join_user',
            db.Column('join_id', db.Integer, db.ForeignKey('joinrequest.id'), primary_key=True),
            db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True))

team_project = db.Table('team_project',
            db.Column('team_id', db.Integer, db.ForeignKey('team.id'), primary_key=True),
            db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True))

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teamname = db.Column(db.String(200), nullable=False)
    filled = db.Column(db.Boolean, unique=False, default=True)
    
    project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete='CASCADE'), nullable=False)
    project = db.relationship('Project', secondary=project_team, backref=db.backref('project_team', lazy='dynamic'), lazy='dynamic')

    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', secondary=user_team, backref=db.backref('user_team', lazy='dynamic'), lazy='dynamic')
   
    join_id = db.Column(db.Integer, db.ForeignKey('joinrequest.id', ondelete='CASCADE'), nullable=False)
    join_requests = db.relationship('Joinrequest', backref=db.backref('team_join', lazy='dynamic'), lazy='dynamic')
    
class Teamabout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(50))

    team_id = db.Column(db.Integer, db.ForeignKey('team.id', ondelete='CASCADE'), nullable=False)
    team = db.relationship('Team', secondary=team_about, backref=db.backref('team_about', lazy='dynamic'), lazy='dynamic')
    

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    projectname = db.Column(db.String(50))
    url = db.Column(db.String(200))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', secondary=user_about, backref=db.backref('user_project', lazy='dynamic'), lazy='dynamic')
    
    team_id = db.Column(db.Integer, db.ForeignKey('team.id', ondelete='CASCADE'), nullable=False)
    team = db.relationship('Team', backref=db.backref('team_project', lazy='dynamic'), lazy='dynamic')

class Projectabout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(50))
    description = db.Column(db.String(50))

    project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete='CASCADE'), nullable=False)
    project = db.relationship('Project', secondary=project_about, backref=db.backref('project_about', lazy='dynamic'), lazy='dynamic')

class Joinrequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # TODO Need to make it an enum 
    # status = db.Column(ENUM('pending', 'denied', 'accepted', 'withdrawn'))
    status = db.Column(db.String(50),nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id', ondelete='CASCADE'), nullable=False)
    team = db.relationship('Team',  secondary=join_team, backref=db.backref('join_team', lazy='dynamic'), lazy='dynamic')

    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User',  secondary=join_user, backref=db.backref('join_user', lazy='dynamic'), lazy='dynamic')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Userabout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(50))
    bio =  db.Column(db.Text(), nullable=False)
    # joined_date = db.Column(db.DateTime(), nullable=False)
    last_accessed = db.Column(db.DateTime())
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', secondary=user_about, backref=db.backref('user_about', lazy='dynamic'), lazy='dynamic')
    
    project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete='CASCADE'), nullable=True)
    project = db.relationship('Project',secondary=userabout_projects, backref=db.backref('userabout_projects', lazy='dynamic'), lazy='dynamic')
    
    team_id = db.Column(db.Integer, db.ForeignKey('team.id', ondelete='CASCADE'), nullable=True)
    team = db.relationship('Team', secondary=userabout_team, backref=db.backref('userabout_team', lazy='dynamic'), lazy='dynamic')

