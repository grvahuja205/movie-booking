from flask.views import MethodView
from flask import make_response, jsonify

class ScreensView(MethodView):
    """
    This is the class for writing the logic for the resource screens
    """

    methods = ['GET']

    def get(self):
        print('inside screen')

        status_code = 200

        response_data = {
            'data':''
        }

        return make_response(jsonify(response_data)), status_code