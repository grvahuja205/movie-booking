from app.models import db, BaseModel

class Theater(BaseModel):
    "This is the theater DB class whoch stores the name of the theater for e.g. 'inox' "
    __tablename__ = 'theater'

    name = db.Column(db.String(300), nullable=False)
    slug = db.Column(db.String(300))

    seating_details = db.relationship('SeatingsRow', back_populates='theater')

    def __str__(self):
        return self.name

    @classmethod
    def get_id_object_mapping(cls):
        return dict(cls.query(cls.id, cls).all())