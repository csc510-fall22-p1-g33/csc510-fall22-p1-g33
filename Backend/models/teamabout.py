# from ..extensions import db
# from sqlalchemy.dialects.mysql import ENUM

# class Teamabout(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     description = db.Column(db.String(50))

#     team_id = db.Column(db.Integer, db.ForeignKey('team.id', ondelete='CASCADE'), nullable=False)
#     team = db.relationship('Team', foreign_keys=['team_id'], backref=db.backref('teamabout'))