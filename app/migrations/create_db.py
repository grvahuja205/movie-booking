from app.models import db, Screen, SeatingsRow, Theater

THEATER_SEATING_DATA = [
    {
        "theater_name" : "Inox",
        "theater_slug": "ionx",
        "screens":[
            {
                "screen_name":"Screen 1",
                "screen_slug":"screen_1",
                "seatings":[
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
                "screen_name": "Screen 2",
                "screen_slug": "screen_2",
                "seatings": [
                    {
                        "name": "A",
                        "slug": "a",
                        "seat_nos": [
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
                        "slug": "b",
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
                        "seat_nos": [
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
            }
        ]
    },
    {
        "theater_name" : "Pvr",
        "theater_slug": "pvr",
        "screens":[
            {
                "screen_name":"Screen 1",
                "screen_slug":"screen_1",
                "seatings":[
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
            },
            {
                "screen_name": "Screen 2",
                "screen_slug": "screen_2",
                "seatings": [
                    {
                        "name": "A",
                        "slug": "a",
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
                        "seat_nos": [
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
    }
]

def create_movie_db_data():
    for theater_seating_details in THEATER_SEATING_DATA:
        theater = Theater(name=theater_seating_details.get('theater_name', ''),
                          slug=theater_seating_details.get('theater_slug'))
        db.session.add(theater)
        db.session.flush()
        for screen_details in theater_seating_details.get('screens'):

            screen = Screen(name=screen_details.get("screen_name"),
                            slug=screen_details.get("screen_slug"),
                            theater_id=theater.id)
            db.session.add(screen)
            db.session.flush()

            for seating_details in screen_details.get('seatings'):
                for row_details in seating_details.get('seat_nos'):
                    row = SeatingsRow(
                        screen_id=screen.id,
                        row_name=seating_details.get("name"),
                        slug=seating_details.get("slug")
                    )
                    row.row_number = row_details[0]
                    row.is_aisle = row_details[1]
                    db.session.add(row)

                db.session.commit()
