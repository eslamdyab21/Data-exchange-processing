from flask import Blueprint

line_graph_blueprint = Blueprint('line_graph', __name__)

from . import routes