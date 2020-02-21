from app.models import db, Theater, SeatingsRow

THEATER_SEATING_DATA = [
    {
        "theater_name" : "Inox",
        "theater_slug": "ionx",
        "seating":[
            {
                "name": "A",
                "slug":"a",
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
                "slug":"b",
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
                "slug": "c",
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
                "slug": "d",
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
        "theater_name" : "Pvr",
        "theater_slug": "pvr",
        "seating":[
            {
                "name": "A",
                "slug": "a",
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
                "slug": "b",
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
                "slug": "c",
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
                "slug": "d",
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
        theater = Theater(name=theater_seating_details.get('theater_name', ''),
                          slug=theater_seating_details.get('theater_slug'))
        db.session.add(theater)
        db.session.flush()
        for seating_details in theater_seating_details.get('seating'):

            for row_number in seating_details.get('seat_nos'):
                row = SeatingsRow(
                    theater_id=theater.id,
                    row_name=seating_details.get("name"),
                    slug=seating_details.get("slug")
                )
                row.row_number = row_number[0]
                row.is_aisle = row_number[1]
                db.session.add(row)

                db.session.commit()
