from flask import request, jsonify
from . import line_graph_selections_blueprint
from services.line_graph_selections.service import get_line_selections


@line_graph_selections_blueprint.route('/line_graph_selections', methods=['GET', 'POST'])
def get_products():    
    data = get_line_selections()
    
    return jsonify(data)

