'Manages all the configurations for the flask app'
from routes.auth import blp as AuthBlueprint
from routes.users import blp as ManagerBlueprint
from utils.config import Config

def flask_config(app):
    'Configuring the flask app'

    app.config["API_TITLE"] = "Task Manager REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["JWT_SECRET_KEY"] = Config.JWT_SECRET_KEY
    app.json.sort_keys = False

def register_blueprints(api):
    'Registering all the blueprints'

    api.register_blueprint(AuthBlueprint,url_prefix='/v1')
    api.register_blueprint(ManagerBlueprint,url_prefix='/v1')