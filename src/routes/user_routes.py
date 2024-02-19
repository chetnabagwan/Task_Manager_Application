from flask.views import MethodView
from flask_jwt_extended import get_jwt, jwt_required
from flask_smorest import Blueprint
from controllers.user_controllers import UserController
from schemas.user_schemas import CreateTasksSchema,UpdateTaskSchema,UpdateProfileSchema

from utils.config import Config

blp = Blueprint('user',__name__)
user_obj = UserController()

@blp.route('/my-profile')
class Myprofile(MethodView):
    @jwt_required()
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def get(self):
        token = get_jwt()
        data = user_obj.myprofile(token)
        return data
    
@blp.route('/update-my-profile')
class UpdateMyprofile(MethodView):

    @blp.arguments(UpdateProfileSchema)
    @jwt_required()
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def put(self,data):
        token = get_jwt()
        return user_obj.update_my_profile(token,data)

@blp.route('/mytasks')
class GetMyTasks(MethodView):

    @jwt_required()
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def get(self):
        token = get_jwt()
        return user_obj.view_my_tasks(token)
               
