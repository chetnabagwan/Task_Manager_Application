from flask.views import MethodView
from flask_jwt_extended import get_jwt, jwt_required
from flask_smorest import Blueprint
from controllers.tasks_controller import TasksController
from schemas.user_schemas import AssignTasksSchema, CreateTasksSchema,UpdateTaskSchema
from utils.config import Config

blp = Blueprint('tasks',__name__)

t_obj =TasksController()

@blp.route('/create-tasks')
class CreateTasks(MethodView):
    '''Route to create new tasks'''

    @blp.arguments(CreateTasksSchema)
    @jwt_required()
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def post(self,data):
        token = get_jwt()
        return t_obj.create_new_tasks(token,data), 201

    
@blp.route('/assign-tasks')
class AssignTasks(MethodView):
    
    @blp.arguments(AssignTasksSchema)
    @jwt_required()
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def post(self,data):
        token=get_jwt()
        return t_obj.assign_tasks_to_user(token,data), 201

        
@blp.route('/update-tasks')
class UpdateMyTasks(MethodView):
    '''Route to update a task'''

    @blp.arguments(UpdateTaskSchema)
    @jwt_required()
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def put(self,data):
        token = get_jwt()
        return t_obj.update_tasks(token,data)
    

@blp.route('/delete-tasks/<string:task_id>')
class DeleteTasks(MethodView):
    '''Route to delete a task'''
    @jwt_required()
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def delete(self,task_id):
        token = get_jwt()
        return t_obj.delete_tasks(token,task_id)