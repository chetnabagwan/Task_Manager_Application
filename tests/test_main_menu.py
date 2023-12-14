"""Test file for main_menu.py"""
import pytest
from utils.config import Config
from main_menu import MainMenu

class TestMainMenu:

    data = [
        ("manager", "1234", "test_msg"),
        ("user", "2134", "test1_msg"),
    ]

    def test_start(self,mocker,capsys):
        mocker.patch('builtins.input',side_effect=['4','2','3','1'])
        mocker.patch('main_menu.Authentication.login', return_value = ['test_user_id', 'test_role'])
        mocker.patch('main_menu.Authentication.sign_up')
        mocker.patch('main_menu.MainMenu.check_role')
        MainMenu.start()
        
        captured = capsys.readouterr()
        print(captured.out)
        assert Config.WRONG_INPUT_ENTERED_MESSAGE in captured.out
        assert Config.LOGIN_SIGNUP_MENU in captured.out


    @pytest.mark.parametrize("role, user_id, expected_output", data)
    def test_check_role(self, role, user_id, expected_output, capsys,mocker):

        mocker.patch('main_menu.Manager')
        mocker.patch('main_menu.User')
        mocker.patch('main_menu.MainMenu.start')
        mocker.patch("main_menu.Config.MANAGER_PROMPT_WLCM", "test_msg")
        mocker.patch("main_menu.Config.USER_PROMPT_WLCM", "test1_msg")
        MainMenu.check_role(role, user_id)
        captured = capsys.readouterr()
        assert expected_output in captured.out