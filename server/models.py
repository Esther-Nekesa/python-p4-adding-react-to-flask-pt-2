from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Movie(db.Model, SerializerMixin):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    director = db.Column(db.String)

    # Standard serialization rules
    serialize_rules = ('-id',)