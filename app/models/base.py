from . import db


class BaseModel(db.Model):
    """
    Base Model for every DB table\model in our DB
    """

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
