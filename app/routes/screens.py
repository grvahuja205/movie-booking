from flask import Blueprint

from app.views.screens import ScreensView

screens_view = Blueprint('screens',__name__, url_prefix='/api')

screens_view.add_url_rule(
    '/screens',
    view_func=ScreensView.as_view('screens_api')
)