from flask import Flask
from db import stores
from dotenv import load_dotenv
from flask_smorest import Api
from resources.store import blp as StoreBlueprint


def create_app():

    app = Flask(__name__)
    # bootstrap = Bootstrap(app)
    # moment = Moment(app)

    load_dotenv()
    app.config['SECRET_KEY'] = 'super-hard to guess string'
    app.config["PROPAGATE_EXCEPTIONS"] = True

    app.config["API_TITLE"] = "Notes REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    api = Api(app)

    api.register_blueprint(StoreBlueprint)

    # your URL routes are in reources/notes.py

    return app
