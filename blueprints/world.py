import flask
from flask import Blueprint

world_api = Blueprint('world_api', __name__)


@world_api.route("/v1/world", methods=["POST"])
def post_world():
    # check if the request is json format
    content_type = flask.request.content_type
    if flask.request.content_type.startswith('application/json'):
        print("yes the content is application/json type")

    # create a response for the user and send it to client
    get_response = {
        "status": "failure",
        "detail": "world_post , this API is for success based data handling. Try /hello for errors",
        "content_type": content_type
    }
    return flask.jsonify(get_response), 400


@world_api.route("/v1/world", methods=["GET"])
def get_world():
    # read data from the parameters.
    username = flask.request.args.get('username', default='NO NAME', type=str)
    password = flask.request.args.get('password', default='NO PASSWORD', type=str)

    get_response = {
        "status": "failure",
        "detail": "world_get"
    }

    # send the response back to the user in json format.
    return flask.jsonify(get_response), 400
