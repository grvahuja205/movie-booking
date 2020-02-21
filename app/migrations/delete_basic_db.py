from app.models import db, Theater as TheaterModel, SeatingsRow as SeatingsRowModel


def delete_data():
    try:
        db.session.query(SeatingsRowModel).delete()
        db.session.query(TheaterModel).delete()
    except Exception as e:
        print(str(e))
        db.session.rollback()
    else:
        db.session.commit()