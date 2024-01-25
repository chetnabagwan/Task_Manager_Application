from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from routes.auth import blp as AuthBlueprint
from utils.config import Config

@Config.config_loader
def create_app():
    app = Flask(__name__)
    app.config["API_TITLE"] = "Task Manager REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    
    api = Api(app) #Connects flask smorest extension to flask app
    
    app.config["JWT_SECRET_KEY"] = "fIqrMcrIKjZqsEZdfwne82n8YsL6F3K0"
    jwt = JWTManager(app) #creating an instance of jwt manager
    
    
    api.register_blueprint(AuthBlueprint)
    
    app.run(debug=True)
    return app

if __name__ == "__main__":
    app = create_app()
    
