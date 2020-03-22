from sqlalchemy import func
from app.models import db, Screen as TheaterModel, SeatingsRow as SeatingRowModel


def get_seating_details(theater_id=None):

    theater_id_seating_details_mapping = db.session.query(
        SeatingRowModel.theater_id.label('theater_id'),
        SeatingRowModel.row_name.label('row_name'),
        func.json_agg(func.json_build_object(
            "row_number", SeatingRowModel.row_number,
            "is_aisle", SeatingRowModel.is_aisle
        )).label('row_details')
    ).group_by(
        SeatingRowModel.theater_id,
        SeatingRowModel.row_name
    ).order_by(
        SeatingRowModel.theater_id,
        SeatingRowModel.row_name
    )

    if theater_id:
        theater_id_seating_details_mapping.filter(SeatingRowModel.theater_id == theater_id)

    return theater_id_seating_details_mapping.all()