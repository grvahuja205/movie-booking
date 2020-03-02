from app.models import db, BaseModel

class SeatingsRow(BaseModel):
    """
    This is a model DB class for row information for each theater.
    This class will have multiple rows per theater and
    will have multiple rows for each row hving different number
    """
    __tablename__ = 'seatings_row'

    screen_id = db.Column(db.Integer, db.ForeignKey('screen.id'), nullable=False)
    screen = db.relationship('Screen', back_populates='seating_details')

    # theater_id = db.Column(db.Integer, db.ForeignKey('theater.id'), nullable=False)
    # theater = db.relationship('Theater', back_populates='seating_details')

    row_name = db.Column(db.String(300), nullable=False) #The name of the row.
    row_number = db.Column(db.Integer, nullable=False) #The row number
    is_aisle = db.Column(db.Boolean, default=False) #Whether aisle or not
    slug = db.Column(db.String(300))

    def __str__(self):
        return self.row_name+self.row_number

    @classmethod
    def get_id_object_mapping(cls):
        return dict(cls.query(cls.id, cls).all())
