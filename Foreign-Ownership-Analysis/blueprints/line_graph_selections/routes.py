from flask import request, jsonify, current_app
from . import line_graph_selections_blueprint
from services.line_graph_selections.service import get_line_selections


@line_graph_selections_blueprint.route('/line_graph_selections', methods=['GET', 'POST'])
def get_data():

    df_merged = current_app.config['df_merged']
    data = get_line_selections(df_merged = df_merged)
    
    return jsonify(data)

