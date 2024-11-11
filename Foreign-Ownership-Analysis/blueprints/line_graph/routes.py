from flask import request, jsonify
from . import line_graph_blueprint
from services.line_graph.service import get_line_data


@line_graph_blueprint.route('/line_graph', methods=['GET', 'POST'])
def get_data():
    data = request.get_json()['selections']

    ticker = data['Tickers']
    country = data['Countries']
    sector = data['Sectors']
    exchange = data['Exchanges']
    y_axis = data['Y-axis']



    df_filtered = get_line_data(ticker = ticker, country = country, sector = sector, exchange = exchange, y_axis = y_axis)
    
    return jsonify(df_filtered.to_json())


# ?ticker=ADNOCGAS UH&country=UAE&sector=Energy&exchange=Abu Dhabi&y_axis=FO%