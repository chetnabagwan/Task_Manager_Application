from utils.config import Config
from users.user_controllers import User

class TestUserControllers:
    """class to test methods of User class"""

    # def test_user_menu(self,mocker,capsys):
    #     """Tests the user_menu function of User class"""

    #     mocker.patch('builtins.input',side_effect = ['1', '2', '3', '4', 'invalid_input', '5'])
    #     mocker.patch.object(User, 'create_new_tasks')
    #     mocker.patch.object(User, 'update_my_tasks')
    #     mocker.patch.object(User, 'view_my_tasks')
    #     mocker.patch.object(User, 'delete_my_tasks')

    #     User('1234').user_menu()
    #     captured = capsys.readouterr()

    #     print(captured.out)
    #     assert Config.NEXT in captured.out
    #     assert Config.USER_PROMPT in captured.out

    def test_create_new_tasks(self,mocker,caplog,capsys):
        """Test function to test create new tasks function"""
        
        mocker.patch('users.user_controllers.InputValidations.task_name_validator', return_value = 'Learn Python')
        mocker.patch('users.user_controllers.InputValidations.task_desc_validator', return_value = 'Decorators and Generators')
        mocker.patch('users.user_controllers.InputValidations.date_validator',return_value = '10-12-2023')
        mocker.patch('users.user_controllers.InputValidations.task_category_validator',return_value = '1')
        mocker.patch('users.user_controllers.add_data')
        
        User('1234').create_new_tasks()
        captured = capsys.readouterr()
        assert Config.TASK_ADDED_SUCCESSFULLY in captured.out
        assert 'User:1234 is creating new tasks.' in caplog.text

    def test_view_my_tasks_negative(self,mocker,caplog,capsys):
        """Test function to test view my tasks function when there are no tasks in database."""
        
        mocker.patch('users.user_controllers.fetch_data',return_value = [])

        User('1234').view_my_tasks()
        captured = capsys.readouterr()
        assert Config.NO_DATA_FOUND in captured.out

        assert 'User:1234 is viewing tasks' in caplog.text

       
    def test_view_my_tasks_positive(self,mocker,caplog,capsys):
        """Test function to test view_my_tasks function when there are tasks available."""
        
        mocker.patch('users.user_controllers.fetch_data',side_effect = ['test_data'])
        mocker.patch('users.user_controllers.tabulate')
      
        User('1234').view_my_tasks()
        captured = capsys.readouterr()

        assert Config.YOUR_TASKS_ARE in captured.out
        assert 'User:1234 is viewing tasks' in caplog.text

    def test_update_my_tasks(self,mocker,caplog,capsys):
        """Test function to test update my tasks function."""

        mocker.patch('users.user_controllers.User.view_my_tasks')
        mocker.patch('users.user_controllers.InputValidations.task_name_validator')
        mocker.patch('builtins.input',side_effect=['4', Config.ONE,'2'])
        mocker.patch('users.user_controllers.InputValidations.date_validator')
        mocker.patch('users.user_controllers.update_data')
        
        User('1234').update_my_tasks()
        captured = capsys.readouterr()

        assert Config.TASK_DUE_DATE_UPDATED in captured.out        
        assert 'User:1234 is updating tasks.' in caplog.text

    def test_delete_my_tasks_negative(self,mocker,capsys,caplog):
        """Test function to test delete my tasks function when there are no tasks in database."""
        
        mocker.patch('users.user_controllers.fetch_data',return_value = [])

        User('1234').delete_my_tasks()
        captured = capsys.readouterr()
        assert Config.NO_TASKS_FOUND_TO_BE_DELETED in captured.out

        assert 'User:1234 is trying to delete tasks.' in caplog.text

    def test_delete_my_tasks_positive(self,mocker,capsys,caplog):
        """Test function to test delete my tasks function when there are tasks present in database."""
        
        mocker.patch('users.user_controllers.fetch_data',return_value = ['test_data'])
        mocker.patch('users.user_controllers.tabulate')
        mocker.patch('users.user_controllers.InputValidations.taskid_validator')
        mocker.patch('users.user_controllers.update_data')

        User('1234').delete_my_tasks()
        captured = capsys.readouterr()
        assert Config.TASKS_THAT_CAN_BE_DELETED in captured.out
        assert Config.TASK_DELETED_SUCCESSFULLY in captured.out

        assert 'User:1234 is trying to delete tasks.' in caplog.text
