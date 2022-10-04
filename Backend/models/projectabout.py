# from ..extensions import db

# from sqlalchemy.dialects.mysql import ENUM

# class Projectabout(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     project_name = db.Column(db.String(50))
#     description = db.Column(db.String(50))

#     project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete='CASCADE'), nullable=False)
#     project = db.relationship('Team',foreign_keys=['project_id'], backref=db.backref('projectabout'))