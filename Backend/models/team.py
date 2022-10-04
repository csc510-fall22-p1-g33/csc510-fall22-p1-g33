# from ..extensions import db

# from sqlalchemy.dialects.mysql import ENUM

# class Team(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     teamname = db.Column(db.String(200), nullable=False)
#     filled = db.Column(db.Boolean, unique=False, default=True)
    
#     project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete='CASCADE'), nullable=False)
#     project = db.relationship('Project',foreign_keys=['project_id'], backref=db.backref('project_team'))

#     user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
#     user = db.relationship('User',foreign_keys=['user_id'], backref=db.backref('user_team'))    
    