from flask_sqlalchemy import SQLAlchemy, Model
from sqlalchemy import Column, DateTime,func


class TimeStampModel(Model):
    """
    Model class for every model
    """
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())


db = SQLAlchemy(model_class=TimeStampModel)