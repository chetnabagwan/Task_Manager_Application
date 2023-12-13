"""Test file for authentication.py file"""
from utils.config import Config
from authentication.authentication import Authentication

class TestAuthentication:
    """class to test Authentication class of authentication module in """
        
    def test_login_successful(self, mocker):
        """Test function to check login success"""

        mocker.patch('builtins.input', side_effect=['chetna'])
        mocker.patch('authentication.authentication.InputValidations.gen_validator', return_value = True)
        mocker.patch('authentication.authentication.pwinput', return_value = '12345')
        mocker.patch('authentication.authentication.hash_pwd', lambda a: 'hashed_pwd')
        mocker.patch('authentication.authentication.fetch_user', side_effect = [(2121,'chetna','hashed_pwd','manager')])
        ret_user_id, ret_role = Authentication.login()
        assert ret_user_id == 2121 and ret_role =='manager'

    def test_login_invalid_credentials(self, mocker,capsys):
        """Test function to check login failure"""

        mocker.patch('builtins.input', return_value='sonal')
        mocker.patch('authentication.authentication.InputValidations.gen_validator', return_value = True)
        mocker.patch('authentication.authentication.pwinput', return_value = 'abc123')
        mocker.patch('authentication.authentication.hash_pwd', return_value = 'hashed_pwd')
        mocker.patch('authentication.authentication.fetch_user', return_value = None)

        data = Authentication.login()
        captured = capsys.readouterr()

        assert data is None
        assert Config.INVALID_CREDENTIALS in captured.out

    def test_sign_up(self,mocker,capsys):
        """Method to test signup function"""

        mocker.patch('builtins.input', return_value='raju')
        mocker.patch('authentication.authentication.InputValidations.gen_validator', return_value = True)
        mocker.patch('authentication.authentication.pwinput', return_value = 'Raju@13')
        mocker.patch('authentication.authentication.InputValidations.password_validator', return_value = True)
        mocker.patch('authentication.authentication.hash_pwd', return_value = 'hashed_pwd')
        mocker.patch('authentication.authentication.add_data')
        Authentication.sign_up()
        captured = capsys.readouterr()
        assert Config.SIGNUP_SUCCESSFUL in captured.out