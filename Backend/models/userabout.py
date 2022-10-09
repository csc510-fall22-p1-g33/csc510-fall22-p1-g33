# from ..extensions import db

# from sqlalchemy.dialects.mysql import ENUM

# user_post = db.Table('user_post',
#             db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
#             db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True))
        
# class Userabout(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     phone = db.Column(db.String(50))
#     bio =  db.Column(db.Text(), nullable=False)
#     joined_date = db.Column(db.DateTime(), nullable=False)
#     last_accessed = db.Column(db.DateTime())
    
#     posts = db.relationship("Post", secondary=user_permissions,          backref=db.backref('user_post', lazy='dynamic'),lazy='dynamic')
 
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
#     user = db.relationship('User', foreign_keys=['user_id'], backref=db.backref('userabout'))
    
#     project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete='CASCADE'), nullable=True)
#     project = db.relationship('Project', foreign_keys=['project_id'], backref=db.backref('userabout'))
    
#     team_id = db.Column(db.Integer, db.ForeignKey('team.id', ondelete='CASCADE'), nullable=True)
#     team = db.relationship('Team', foreign_keys=['team_id'],  backref=db.backref('userabout'))