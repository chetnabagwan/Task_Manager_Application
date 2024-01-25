from flask import request
from flask.views import MethodView
from flask_jwt_extended import get_jwt, jwt_required
from flask_smorest import Blueprint, abort
from schemas import AuthSchema
from business.authentication import Authentication

blp = Blueprint('authentication',__name__)

@blp.post("/login")
class Authcontroller(MethodView):
    @blp.arguments(AuthSchema)
    def login_controller(self,login_data):
            username = login_data['username']
            password = login_data['password']
            try:    
                user_data = Authentication.login(username,password)
            except:
                raise In
            user_id,role = user_data
         Invalidcredentials:
            abort(401,message="unauthenticated user")


