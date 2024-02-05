from flask.views import MethodView
from flask_jwt_extended import get_jwt, jwt_required
from flask_smorest import Blueprint
from controllers.manager_controller import ManagerController
from schemas.user_schemas import AssignTasksSchema

from utils.config import Config

blp = Blueprint('manager',__name__)
man_obj = ManagerController()

@blp.route('/users')
class Allusers(MethodView):
    @jwt_required()
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def get(self):
        token = get_jwt()
        return man_obj.get_all_users(token)
    
@blp.route('/assign-tasks')
class AssignTasks(MethodView):
    @blp.arguments(AssignTasksSchema)
    @jwt_required()
    # @blp.doc(parameters=Config.PARAMS)
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def post(self,data):
        token=get_jwt()
        man_obj.assign_tasks_to_user(token,data)