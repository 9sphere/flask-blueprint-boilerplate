import flask
from flask import Blueprint

hello_api = Blueprint('hello_api', __name__)


@hello_api.route("/v1/hello", methods=["POST"])
def post_hello():
    # check if the request is json format
    content_type = flask.request.content_type
    if content_type.startswith('application/json'):
        print("yes the content is application/json type")

    # read the payload from REST api call
    json_payload = flask.request.get_json()
    name = 'NONE GIVEN'
    if "name" in json_payload:
        name = flask.request.get_json()['name']

    # write all the other processing here
    #
    #

    # create a response for the user and send it to client
    post_response = {
        "status": "success",
        "detail": "hello_post, this API is for success based data handling. Try /world for errors",
        "content_type": content_type,
        "name": name
    }
    return flask.jsonify(post_response)


@hello_api.route("/v1/hello", methods=["GET"])
def get_hello():
    # read data from the parameters.
    username = flask.request.args.get('username', default='NO NAME', type=str)
    password = flask.request.args.get('password', default='NO PASSWORD', type=str)

    get_response = {
        "status": "success",
        "detail": "hello_get, this API is for success based data handling. Try /world for errors",
        "username": username,
        "password": password
    }

    # send the response back to the user in json format.
    return flask.jsonify(get_response)
