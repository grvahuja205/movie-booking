from sqlalchemy import func
from app.models import db, Theater as TheaterModel, SeatingsRow as SeatingRowModel


class SeatingDetailsHelper():

    def get_theater_id_rows_mapping(self):
        theater_id_rows_mapping = db.session.query(
            SeatingRowModel.theater_id,
            func.array_agg(SeatingRowModel.id)
        ).join(
            TheaterModel,
            TheaterModel.id == SeatingRowModel.theater_id
        ).group_by(

        )

def get_seating_details():
    theater_id_seating_details_mapping = dict(db.session.query(
        SeatingRowModel.theater_id,
        func.json_agg(func.json_build_objet(
            SeatingRowModel.row_name , SeatingRowModel
        ))
    ).group_by(
        SeatingRowModel.theater_id
    ).all())

    return theater_id_seating_details_mapping