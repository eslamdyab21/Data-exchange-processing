from flask import request, jsonify
from . import line_graph_blueprint
from services.line_graph.service import get_line_data


@line_graph_blueprint.route('/line_graph', methods=['GET', 'POST'])
def get_products():
    ticker = request.args.get('ticker')
    country = request.args.get('country')
    sector = request.args.get('sector')
    exchange = request.args.get('exchange')
    y_axis = request.args.get('y_axis')

    df_filtered = get_line_data(ticker = ticker, country = country, sector = sector, exchange = exchange, y_axis = y_axis)
    

    return jsonify(df_filtered.to_json())


# ?ticker=ADNOCGAS UH&country=UAE&sector=Energy&exchange=Abu Dhabi&y_axis=FO%