from ..extensions import db

from sqlalchemy.dialects.mysql import ENUM


associate_users_projects = db.Table('associate_users_projects',
            db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
            db.Column('project_id', db.Integer, db.ForeignKey('project.id')))
            
associate_users_joinrequests = db.Table('associate_users_joinrequests',
            db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
            db.Column('joinrequest_id', db.Integer, db.ForeignKey('joinrequest.id')))

associate_users_teams = db.Table('associate_users_teams',
            db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
            db.Column('team_id', db.Integer, db.ForeignKey('team.id')))

# associate_teams_projects = db.Table('associate_teams_projects',
            # db.Column('team_id', db.Integer, db.ForeignKey('team.id')),
            # db.Column('project_id', db.Integer, db.ForeignKey('project.id')))

# user_project = db.Table('user_project',
#             db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
#             db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True))

# user_team = db.Table('user_team',
#             db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
#             db.Column('team_id', db.Integer, db.ForeignKey('team.id'), primary_key=True))

# userabout_projects = db.Table('userabout_projects',
#             db.Column('about_id', db.Integer, db.ForeignKey('userabout.id'), primary_key=True),
#             db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True))

# userabout_team = db.Table('userabout_team',
#             db.Column('about_id', db.Integer, db.ForeignKey('userabout.id'), primary_key=True),
#             db.Column('teadm_id', db.Integer, db.ForeignKey('team.id'), primary_key=True))

# user_about = db.Table('user_about',
#             db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
#             db.Column('about_id', db.Integer, db.ForeignKey('userabout.id'), primary_key=True))

# project_about = db.Table('project_about',
#             db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True),
#             db.Column('about_id', db.Integer, db.ForeignKey('projectabout.id'), primary_key=True))

# team_about = db.Table('team_about',
#             db.Column('team_id', db.Integer, db.ForeignKey('team.id'), primary_key=True),
#             db.Column('about_id', db.Integer, db.ForeignKey('teamabout.id'), primary_key=True))

# project_team = db.Table('project_team',
#             db.Column('team_id', db.Integer, db.ForeignKey('team.id'), primary_key=True),
#             db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True))

# join_team = db.Table('join_team',
#             db.Column('join_id', db.Integer, db.ForeignKey('joinrequest.id'), primary_key=True),
#             db.Column('team_id', db.Integer, db.ForeignKey('team.id'), primary_key=True))

# team_join = db.Table('team_join',
#             db.Column('join_id', db.Integer, db.ForeignKey('joinrequest.id'), primary_key=True),
#             db.Column('team_id', db.Integer, db.ForeignKey('team.id'), primary_key=True))

# join_user = db.Table('join_user',
#             db.Column('join_id', db.Integer, db.ForeignKey('joinrequest.id'), primary_key=True),
#             db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True))

# team_project = db.Table('team_project',
#             db.Column('team_id', db.Integer, db.ForeignKey('team.id'), primary_key=True),
#             db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True))

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete='CASCADE'))
    project = db.relationship('Project', back_populates='teams')

    users = db.relationship('User', secondary=associate_users_teams, back_populates='teams')
    join_requests = db.relationship('Joinrequest', back_populates='team', cascade='all, delete')

    filled = db.Column(db.Boolean, nullable=False)
    # teamname = db.Column(db.String(200), nullable=False)
    # filled = db.Column(db.Boolean, unique=False, default=True)
    
    # project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete='CASCADE'), nullable=False)
    # project = db.relationship('Project', secondary=project_team, backref=db.backref('project_team', lazy='dynamic'), lazy='dynamic')

    # user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    # user = db.relationship('User', secondary=user_team, backref=db.backref('user_team', lazy='dynamic'), lazy='dynamic')
   
    # join_id = db.Column(db.Integer, db.ForeignKey('joinrequest.id', ondelete='CASCADE'), nullable=False)
    # join_requests = db.relationship('Joinrequest', secondary=team_join, backref=db.backref('team_join', lazy='dynamic'), lazy='dynamic')
    
class Teamabout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    team_id = db.Column(db.Integer, db.ForeignKey('team.id', ondelete='CASCADE'))
    team = db.relationship('Team', backref=db.backref('about', uselist=False))

    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    # description = db.Column(db.String(50))

    # team_id = db.Column(db.Integer, db.ForeignKey('team.id', ondelete='CASCADE'), nullable=False)
    # team = db.relationship('Team', secondary=team_about, backref=db.backref('team_about', lazy='dynamic'), lazy='dynamic')
    

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    users = db.relationship('User', secondary=associate_users_projects, back_populates='projects')
    teams = db.relationship('Team', back_populates='project', cascade='all, delete')
    
    # projectname = db.Column(db.String(50))
    # url = db.Column(db.String(200))

    # user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    # user = db.relationship('User', secondary=user_project, backref=db.backref('user_project', lazy='dynamic'), lazy='dynamic')
    
    # team_id = db.Column(db.Integer, db.ForeignKey('team.id', ondelete='CASCADE'), nullable=False)
    # team = db.relationship('Team', secondary=team_project, backref=db.backref('team_project', lazy='dynamic'), lazy='dynamic')

class Projectabout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete='CASCADE'))
    project = db.relationship('Project', backref=db.backref('about', uselist=False))

    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text(), nullable=False)

class Joinrequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    user = db.relationship('User', back_populates='join_requests')
    
    team_id = db.Column(db.Integer, db.ForeignKey('team.id', ondelete='CASCADE'))
    team = db.relationship('Team', back_populates='join_requests')
    
    # TODO Need to make it an enum 
    # status = db.Column(ENUM('pending', 'denied', 'accepted', 'withdrawn'))
    status = db.Column(db.String(50),nullable=False)

    # team_id = db.Column(db.Integer, db.ForeignKey('team.id', ondelete='CASCADE'), nullable=False)
    # team = db.relationship('Team',  secondary=join_team, backref=db.backref('join_team', lazy='dynamic'), lazy='dynamic')

    # user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    # user = db.relationship('User',  secondary=join_user, backref=db.backref('join_user', lazy='dynamic'), lazy='dynamic')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    projects = db.relationship('Project', secondary=associate_users_projects, back_populates='users')
    join_requests = db.relationship('Joinrequest', back_populates='user', cascade='all, delete')
    teams = db.relationship('Team', secondary=associate_users_teams, back_populates='users')


class Userabout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    user = db.relationship('User', backref=db.backref('about', uselist=False))

    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    bio =  db.Column(db.Text())