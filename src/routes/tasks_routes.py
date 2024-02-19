from flask.views import MethodView
from flask_jwt_extended import get_jwt, jwt_required
from flask_smorest import Blueprint
from controllers.user_controllers import UserController
from schemas.user_schemas import CreateTasksSchema,UpdateTaskSchema

from utils.config import Config

blp = Blueprint('tasks',__name__)



@blp.route('/create-tasks')
class CreateTasks(MethodView):
    '''Route to create new tasks'''

    @blp.arguments(CreateTasksSchema)
    @jwt_required()
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def post(self,data):
        token = get_jwt()
        return user_obj.create_new_tasks(token,data)

    
@blp.route('/assign-tasks')
class AssignTasks(MethodView):
    @blp.arguments(AssignTasksSchema)
    @jwt_required()
    # @blp.doc(parameters=Config.PARAMS)
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def post(self,data):
        token=get_jwt()
        man_obj.assign_tasks_to_user(token,data)


@blp.route('/update-tasks')
class UpdateTasks(MethodView):
    '''Route to update a task'''

    @blp.arguments(UpdateTaskSchema)
    @jwt_required()
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def put(self,data):
        token = get_jwt()
        return user_obj.create_new_tasks(token,data)
    

@blp.route('/create-tasks')
class DeleteTasks(MethodView):
    '''Route to delete a task'''
#path parameter task_id
    @jwt_required()
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def delete(self,data):
        token = get_jwt()
        return user_obj.create_new_tasks(token,data)
    
@blp.route('/update-task-status')
class UpdateStatusOfAssignedTasks(MethodView):
    @blp.arguments(UpdateTaskSchema)
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def put(self,data):
        token = get_jwt()
        man_obj.update_taskstatus(token,data)
