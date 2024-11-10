from flask import Blueprint

line_graph_selections_blueprint = Blueprint('line_graph_selections', __name__)

from . import routes