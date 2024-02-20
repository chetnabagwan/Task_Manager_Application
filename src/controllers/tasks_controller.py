import logging
from flask_smorest import abort
from business.tasks import Task
from utils.helper_functions import DataNotFoundError,NotAuthorizedError,create_id,date_today
from utils.config import Config

logger = logging.getLogger('main.tasks_controllers')

tb_obj = Task()

class TasksController:
    def create_new_tasks(self,token,data):
            """This method creates new task for user"""
            logger.info('User is creating new tasks.')

            try:    
                r = token['role']
                if r != 'user':
                    logger.warning(f'Unauthorized user {token["sub"]} is assigning tasks to users.')
                    raise NotAuthorizedError
                user_id = token['sub']
                task_id = create_id()
                task_name = data['task_name']
                task_desc = data['task_desc']
                today_date = date_today()
                due_date = data['due_date']
                category = data['category']     
                tb_obj.create_new_tasks(task_id,user_id,task_name,task_desc,today_date,due_date,category)
                return {"message":"Task created successfully"}
            except Exception as e:
                raise e


    def assign_tasks_to_user(self,token,data):
        '''This method assigns tasks to a user.'''

        logger.info(f'Manager is assigning tasks to users.')
        try:    
            r = token['role']
            if r != 'manager':
                logger.warning(f'Unauthorized user {token["sub"]} is assigning tasks to users.')
                raise NotAuthorizedError
            man_id = token['sub']
            task_id = create_id()
            user_id = data['user_id']
            task_name = data['task_name']
            task_desc = data['task_desc']
            today_date = date_today()
            due_date = data['due_date']
            category = data['category']
            tb_obj.assign_tasks_to_user_logic(task_id,user_id,task_name,task_desc,today_date,due_date,category,man_id)
            return {"message":"Task assigned successfully"}

        except Exception as e:
            raise e


    def update_tasks(self,token,data):
        """This method helps user to update his/her tasks. User can update both status and duedate of a task"""
        
        logger.info('User is updating tasks.')
        try:
            user_id = token['sub']
            task_id = data['task_id']
            task_name = data['task_name']
            task_desc = data['task_desc']
            due_date = data['due_date']
            is_completed = data['is_completed'] 
            r = token['role']
            if r == 'user':
                tb_obj.update_my_tasks(user_id,task_id,task_name,task_desc,due_date,is_completed)
                return{'message':"Task updated successfully"}
            if r == 'manager':
                tb_obj.update_assigned_tasks(user_id,task_id,task_name,task_desc,due_date,is_completed)
                return{'message':"Task updated successfully"}
        except DataNotFoundError :
            abort(404,message = 'No task found with the given task id')
 
    
    def delete_tasks(self,token,data):
        """This method deletes a selected task."""

        logger.info('User is trying to delete tasks.')
        try:
            task_id = data['task_id']
            r = token['role']
            if r == 'user':
                tb_obj.delete_my_tasks(task_id)
                return{'message':"Task deleted successfully"}
            if r == 'manager':
                tb_obj.delete_assigned_tasks(task_id)
                return{'message':"Task deleted successfully"}
        except DataNotFoundError :
            abort(404,message = "No task found with the given task id")
