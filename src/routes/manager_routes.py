from flask.views import MethodView
from flask_jwt_extended import get_jwt, jwt_required
from flask_smorest import Blueprint
from controllers.manager_controllers import ManagerController
from schemas.user_schemas import AssignTasksSchema,UpdateTaskSchema

from utils.config import Config

blp = Blueprint('manager',__name__)
man_obj = ManagerController()

@blp.route('/users')
class Allusers(MethodView):
    '''Route to view all users'''
    @jwt_required()
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def get(self):
        token = get_jwt()
        return man_obj.get_all_users(token)


@blp.route('/task-status')
class ViewStatusOfAssignedTasks(MethodView):
   
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def get(self):
        token = get_jwt()
        man_obj.view_status_of_assigned_tasks(token)



