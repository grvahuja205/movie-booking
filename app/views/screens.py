from flask.views import MethodView
from flask import make_response, jsonify
from collections import defaultdict

from .helpers import get_seating_details
from app.models import Theater as TheaterModel, SeatingsRow as SeatingRowModel

class ScreensView(MethodView):
    """
    This is the class for writing the logic for the resource screens
    """

    methods = ['GET']

    def get(self):
        print('inside screen')

        status_code = 200

        seating_details = get_seating_details()

        theater_id_theater_objet_mapping = TheaterModel.get_id_object_mapping()

        seating_row_id_seating_row_object = SeatingRowModel.get_id_object_mapping()

        seating_mapping = defaultdict(list)

        for theater_id, row_details in seating_details.items():
            pass

        response_data = {
            'data':''
        }

        return make_response(jsonify(response_data)), status_code