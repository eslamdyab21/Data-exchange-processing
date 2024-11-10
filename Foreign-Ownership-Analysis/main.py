from flask import Flask
from flask_cors import CORS

from blueprints.line_graph import line_graph_blueprint
from blueprints.line_graph_selections import line_graph_selections_blueprint

from services.line_graph import *
from services.line_graph_selections import *


app = Flask(__name__)
CORS(app, origins="*")


# Register Blueprints
app.register_blueprint(line_graph_blueprint)
app.register_blueprint(line_graph_selections_blueprint)



app.run(debug=True, port=8000)
