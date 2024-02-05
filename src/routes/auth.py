import logging
from flask.views import MethodView
from flask_jwt_extended import get_jwt, jwt_required
from flask_smorest import Blueprint
from schemas.auth_schemas import RegisterSchema,LoginSchema
from controllers.auth_controller import AuthController

blp = Blueprint('authentication',__name__)

auth_obj = AuthController()

logger = logging.getLogger(__name__)
@blp.route("/register")
class Register(MethodView):
    @blp.arguments(RegisterSchema)
    def post(self,register_data):
        return auth_obj.RegisterController(register_data)
    
    
@blp.route("/login")
class Login(MethodView):
    @blp.arguments(LoginSchema)
    def post(self,login_data: dict):
        return auth_obj.LoginController(login_data)
        

@blp.route("/logout")
class Logout(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt().get('jti')
        return auth_obj.LogoutController(jti)