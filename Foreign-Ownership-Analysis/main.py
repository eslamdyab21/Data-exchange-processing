from flask import Flask
from blueprints.line_graph import line_graph_blueprint



app = Flask(__name__)


# Register Blueprints
app.register_blueprint(line_graph_blueprint)


app.run(debug = True)
app.run() 