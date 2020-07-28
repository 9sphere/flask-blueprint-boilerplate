from flask import Flask
from flask_cors import CORS

from blueprints.hello import hello_api
from blueprints.world import world_api

app = Flask(__name__)

# adding CORS to handle cross origin request
CORS(app)

app.secret_key = '/FCCk{Pz_fS+5FsW{c*MV=hP$um>#b]3W?X'

# registering the APIs
app.register_blueprint(hello_api)
app.register_blueprint(world_api)

if __name__ == "__main__":
    app.run(debug=True)