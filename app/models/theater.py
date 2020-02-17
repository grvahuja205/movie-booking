from app.models import db, BaseModel

class Theater(BaseModel):
    "This is the theater DB class whoch stores the name of the theater for e.g. 'inox' "
    __tablename__ = 'theater'

    name = db.Column(db.String(300), nullable=False)

    seating_details = db.relationship('SeatingsRow', back_populates='theater')