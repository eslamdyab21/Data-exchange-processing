from flask import jsonify, request
from . import line_graph_blueprint



@line_graph_blueprint.route('/line_graph', methods=['GET', 'POST'])
def get_products():
    ticker = request.args.get('ticker')
    country = request.args.get('country')
    sector = request.args.get('sector')
    exchange = request.args.get('exchange')
    print(ticker)

    return ticker


