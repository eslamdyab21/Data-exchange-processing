from flask import Flask
from flask_cors import CORS

from blueprints.line_graph import line_graph_blueprint
from blueprints.line_graph_selections import line_graph_selections_blueprint

from services.line_graph import *
from services.line_graph_selections import *

from services.load_merged_data.service import load_merged_data

df_merged = load_merged_data()


app = Flask(__name__)
CORS(app, origins="*")


# Register Blueprints
app.register_blueprint(line_graph_blueprint)
app.register_blueprint(line_graph_selections_blueprint)


# Load data
app.config['df_merged'] = df_merged



app.run(debug=True, port=8000)
