from app.models import db, BaseModel

class Screen(BaseModel):
    "This is the screen DB class whoch stores the name of the screen for e.g. 'screen 1' "
    __tablename__ = 'screen'

    name = db.Column(db.String(300), nullable=False)
    slug = db.Column(db.String(300))

    theater_id = db.Column(db.Integer, db.ForeignKey('theater.id'), nullable=False)
    theater = db.relationship('Theater', back_populates='screen_details')

    seating_details = db.relationship('SeatingsRow', back_populates='screen')

    def __str__(self):
        return self.name

    @classmethod
    def get_id_object_mapping(cls):
        return dict(cls.query(cls.id, cls).all())