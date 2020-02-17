from app.models import db, Theater, SeatingsRow

THEATER_SEATING_DATA = [
    {
        "theater_name" : "inox",
        "seating":[
            {
                "name": "A",
                "seat_nos" :[
                    (1, True),
                    (2, False),
                    (3, False),
                    (4, True),
                    (5, True),
                    (6, False),
                    (7, False),
                    (8, True)
                ],
            },
            {
                "name": "B",
                "seat_nos": [
                    (1, False),
                    (2, True),
                    (3, True),
                    (4, False),
                    (5, False),
                    (6, True),
                    (7, True),
                    (8, False)
                ],
            },
            {
                "name": "C",
                "seat_nos": [
                    (1, False),
                    (2, False),
                    (3, False),
                    (4, False),
                    (5, False),
                    (6, False),
                    (7, True),
                    (8, False)
                ],
            },
            {
                "name": "D",
                "seat_nos":[
                    (1, True),
                    (2, False),
                    (3, False),
                    (4, False),
                    (5, False),
                    (6, False),
                    (7, False),
                    (8, True)
                ]

            }
        ]
    },
    {
        "theater_name" : "pvr",
        "seating":[
            {
                "name": "A",
                "seat_nos" :[
                    (1, False),
                    (2, False),
                    (3, False),
                    (4, False),
                    (5, False),
                    (6, False),
                    (7, True),
                    (8, False)
                ],
            },
            {
                "name": "B",
                "seat_nos": [
                    (1, True),
                    (2, False),
                    (3, False),
                    (4, False),
                    (5, False),
                    (6, False),
                    (7, False),
                    (8, True)
                ],
            },
            {
                "name": "C",
                "seat_nos": [
                    (1, False),
                    (2, True),
                    (3, True),
                    (4, False),
                    (5, False),
                    (6, True),
                    (7, True),
                    (8, False)
                ],
            },
            {
                "name": "D",
                "seat_nos":[
                    (1, True),
                    (2, False),
                    (3, False),
                    (4, True),
                    (5, True),
                    (6, False),
                    (7, False),
                    (8, True)
                ]

            }
        ]
    }
]

def create_movie_db_data():
    for theater_seating_details in THEATER_SEATING_DATA:
        theater = Theater(name=theater_seating_details.get('theater_name', ''))
        db.session.add(theater)
        db.session.flush()
        for seating_details in theater_seating_details.get('seating'):

            for row_number in seating_details.get('seat_nos'):
                row = SeatingsRow(
                    theater_id=theater.id,
                    row_name=seating_details.get("name")
                )
                row.row_number = row_number[0]
                row.is_aisle = row_number[1]
                db.session.add(row)

                db.session.commit()
