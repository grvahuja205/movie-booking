from flask import Blueprint

from app.views.theater_screen_seating import TheaterScreenSeating

theater_screen_view = Blueprint('screen',__name__, url_prefix='/api')

theater_screen_view.add_url_rule(
    '/theater/<int:theater_id>',
    view_func=TheaterScreenSeating.as_view('screen_seating_api')
)