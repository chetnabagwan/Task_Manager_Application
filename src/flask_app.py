from flask import Flask
from flask_smorest import Api
from routes.auth import blp as AuthBlueprint
from routes.users import blp as ManagerBlueprint
from utils.config import Config


app = Flask(__name__)
app.config["API_TITLE"] = "Task Manager REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app) #Connects flask smorest extension to flask app

app.config["JWT_SECRET_KEY"] = Config.JWT_SECRET_KEY

api.register_blueprint(AuthBlueprint)
api.register_blueprint(ManagerBlueprint)

app.run(debug=True)



