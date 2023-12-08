"""Test file for authentication.py file"""
import pytest
from src.utils.config import Config
from src.authentication.authentication import Authentication

class TestAuthentication:
    """class to test Authentication class of authentication module in src."""
        
    def test_login_successful(self, mocker):
        """Test function to check login success"""

        mocker.patch('builtins.input', side_effect=['chetna'])
        mocker.patch('src.authentication.authentication.InputValidations.gen_validator', return_value = True)
        mocker.patch('src.authentication.authentication.pwinput', return_value = '12345')
        mocker.patch('src.authentication.authentication.hash_pwd', lambda a: 'hashed_pwd')
        mocker.patch('src.authentication.authentication.fetch_user', side_effect = [(2121,'chetna','hashed_pwd','manager')])
        ret_user_id, ret_role = Authentication.login()
        assert ret_user_id == 2121 and ret_role =='manager'

    def test_login_invalid_credentials(self, mocker,capsys):
        """Test function to check login failure"""

        mocker.patch('builtins.input', return_value='sonal')
        mocker.patch('src.authentication.authentication.InputValidations.gen_validator', return_value = True)
        mocker.patch('src.authentication.authentication.pwinput', return_value = 'abc123')
        mocker.patch('src.authentication.authentication.hash_pwd', return_value = 'hashed_pwd')
        mocker.patch('src.authentication.authentication.fetch_user', return_value = None)

        data = Authentication.login()
        captured = capsys.readouterr()

        assert data is None
        assert Config.INVALID_CREDENTIALS in captured.out

    def test_signup(self,mocker,capsys):
        """Method to test signup function"""

        mocker.patch('builtins.input', return_value='raju')
        mocker.patch('src.authentication.authentication.InputValidations.gen_validator', return_value = True)
        mocker.patch('src.authentication.authentication.pwinput', return_value = 'Raju@13')
        mocker.patch('src.authentication.authentication.InputValidations.password_validator', return_value = True)
        mocker.patch('src.authentication.authentication.hash_pwd', return_value = 'hashed_pwd')
        mocker.patch('src.authentication.authentication.add_data')
        Authentication.signUp()
        captured = capsys.readouterr()
        assert Config.SIGNUP_SUCCESSFUL in captured.out
    











# def mock_fetch_user(query, username, hashed_password):
#     # Implement your mock behavior here
#     pass

# def test_login_successful(monkeypatch, capsys):
#     # Mock user input and fetch_user function for a successful login
#     username_input = "valid_username"
#     password_input = "valid_password"
#     expected_result = (1, "user_role")

#     monkeypatch.setattr('builtins.input', lambda _: username_input)
#     monkeypatch.setattr('your_module.pwinput', lambda prompt: password_input)
#     monkeypatch.setattr('your_module.fetch_user', mock_fetch_user)

#     # Mock print statements
#     with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
#         result = Authentication.login()

#     captured = capsys.readouterr()

#     assert Config.LOGIN_SUCCESSFUL in mock_stdout.getvalue()
#     assert result == expected_result

# def test_login_failed_invalid_username(monkeypatch, capsys):
#     # Mock user input and fetch_user function for a failed login (invalid username)
#     username_input = "invalid_username"
#     password_input = "valid_password"

#     monkeypatch.setattr('builtins.input', lambda _: username_input)
#     monkeypatch.setattr('your_module.pwinput', lambda prompt: password_input)
#     monkeypatch.setattr('your_module.fetch_user', mock_fetch_user)

#     # Mock print statements
#     with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
#         Authentication.login()

#     captured = capsys.readouterr()

#     assert Config.LOGIN_FAILED in mock_stdout.getvalue()

# def test_login_failed_invalid_credentials(monkeypatch, capsys):
#     # Mock user input and fetch_user function for a failed login (invalid credentials)
#     username_input = "valid_username"
#     password_input = "invalid_password"

#     monkeypatch.setattr('builtins.input', lambda _: username_input)
#     monkeypatch.setattr('your_module.pwinput', lambda prompt: password_input)
#     monkeypatch.setattr('your_module.fetch_user', mock_fetch_user)

#     # Mock print statements
#     with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
#         Authentication.login()

#     captured = capsys.readouterr()

#     assert Config.INVALID_CREDENTIALS in mock_stdout.getvalue()


