from flask.views import MethodView
from collections import defaultdict
from flask import make_response, jsonify

from .helpers import get_seating_details
from app.models.helpers import get_model_id_model_object_mapping
from app.models import Screen as TheaterModel

class TheaterScreenSeating(MethodView):
    """
    This class would represent a particular screen
    """
    methods = ['GET']

    def get(self, theater_id):
        status_code = 200

        seating_details = get_seating_details(theater_id=theater_id)

        theater_id_theater_objet_mapping = get_model_id_model_object_mapping(TheaterModel)

        seating_mapping = defaultdict(list)

        for theater_row_details in seating_details:
            theater_details = defaultdict(list)
            if seating_mapping.get(theater_id_theater_objet_mapping.get(theater_row_details[0]).name):
                theater_details[theater_row_details[1]].append(theater_row_details[2])
                seating_mapping.get(theater_id_theater_objet_mapping.get(theater_row_details[0]).name).append(
                    theater_details)
            else:
                theater_details[theater_row_details[1]] = theater_row_details[2]
                seating_mapping[theater_id_theater_objet_mapping.get(theater_row_details[0]).name] = [theater_details]

        response_data = {
            'data': seating_mapping
        }

        return make_response(jsonify(response_data)), status_code