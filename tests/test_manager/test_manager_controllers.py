"""Test file to test manager_controllers.py"""
from utils.config import Config
from manager.manager_controllers import Manager


class TestManager :
    """class to test methods of Manager class"""

    def test_manager_menu(self, mocker, capsys):
        """test function to test manager_menu function"""
       
        mocker.patch('builtins.input', side_effect=['1', '2', '3', '4', 'invalid_input', '5'])
        mocker.patch.object(Manager, 'view_all_users')
        mocker.patch.object(Manager, 'assign_tasks_to_user')
        mocker.patch.object(Manager, 'view_status_of_assigned_tasks')
        mocker.patch.object(Manager, 'update_status_of_assigned_task')

        Manager('1234').manager_menu()
        captured = capsys.readouterr()

        assert Config.NEXT in captured.out
        assert Config.MANAGER_PROMPT in captured.out

    def test_view_all_users(self, mocker, caplog):
        """Test function to test view all users function"""

        mocker.patch('manager.manager_controllers.display_data')
        mocker.patch('manager.manager_controllers.tabulate')
        
        Manager('1234').view_all_users()
        assert 'Manager:1234 is viewing all users' in caplog.text

    def test_assign_tasks_to_user(self,mocker,capsys,caplog):
        """Test function to test assign tasks to user function of manager class"""
    
        mocker.patch('manager.manager_controllers.Manager.view_all_users')
        mocker.patch('manager.manager_controllers.InputValidations.userid_validator', return_value = '1234')
        mocker.patch('manager.manager_controllers.InputValidations.task_name_validator', return_value = 'Learn Python')
        mocker.patch('manager.manager_controllers.InputValidations.task_desc_validator', return_value = 'Decorators and Generators')
        mocker.patch('manager.manager_controllers.InputValidations.date_validator',return_value = '10-12-2023')
        mocker.patch('manager.manager_controllers.InputValidations.task_category_validator',return_value = '1')
        mocker.patch('manager.manager_controllers.add_data')
        
        Manager('1234').assign_tasks_to_user()
        captured = capsys.readouterr()
        assert Config.TASK_ASSIGNED_SUCCESSFULLY in captured.out
        assert 'Manager:1234 is assigning tasks to users.' in caplog.text

    def test_view_status_of_assigned_tasks(self,mocker,caplog,capsys):
        """Test function to test view_status_of_assigned_tasks function."""
        
        mocker.patch('manager.manager_controllers.fetch_data', side_effect = [[], 'test_data'])
        mocker.patch('manager.manager_controllers.tabulate')
        Manager('1234').view_status_of_assigned_tasks()
        captured = capsys.readouterr()

        assert Config.NO_DATA_FOUND in captured.out
        assert 'Manager:1234 is trying to view status of assigned tasks' in caplog.text

    def test_positive_update_status_of_assigned_task(self,mocker,caplog,capsys):
        """Test function to test update_status_of_assigned_task function when there are tasks available to update."""
        
        mocker.patch('manager.manager_controllers.fetch_data',side_effect = ['test_data',(),'test_data2'])
        mocker.patch('manager.manager_controllers.tabulate')
        mocker.patch('manager.manager_controllers.InputValidations.taskid_validator')
        mocker.patch('manager.manager_controllers.InputValidations.task_status_validator')
        mocker.patch('manager.manager_controllers.update_data')

        Manager('1234').update_status_of_assigned_task()
        captured = capsys.readouterr()
        assert Config.WHICH_TASK in captured.out
        assert Config.TASKID_NOT_FOUND in captured.out 
        assert Config.TASK_STATUS_UPDATED in captured.out

        assert 'Manager:1234 is updating status of assigned tasks' in caplog.text

    def test_negative_update_status_of_assigned_task(self,mocker,caplog,capsys):
        """Test function to test update_status_of_assigned_task function when there are no tasks available to update."""
        
        mocker.patch('manager.manager_controllers.fetch_data',return_value = [])

        Manager('1234').update_status_of_assigned_task()
        captured = capsys.readouterr()
        assert Config.NO_DATA_FOUND in captured.out

        assert 'Manager:1234 is updating status of assigned tasks' in caplog.text