"""Test file for main_menu.py"""
from utils.config import Config
from main_menu import MainMenu

class TestMainMenu:
    def test_start(self,mocker,capsys):
        mocker.patch('builtins.input',side_effect=['4','2','3','1'])
        mocker.patch('main_menu.Authentication.login', return_value = ['test_user_id', 'test_role'])
        mocker.patch('main_menu.Authentication.sign_up')
        mocker.patch('main_menu.welcomemsg_role')
        MainMenu.start()
        
        captured = capsys.readouterr()
        assert Config.WRONG_INPUT_ENTERED_MESSAGE in captured.out
        assert Config.LOGIN_SIGNUP_MENU in captured.out


    def test_user_has_permission(self,mocker):
        mocker.patch('main_menu.user_has_permission.checkrole',ret)
        # mocker.patch('main_menu.manager_menu')
        # mocker.patch('main_menu.user_menu')
        # mocker.patch('main_menu.Main_Menu.start')
    
        # MainMenu.user_has_permission()
        
        
        

    def test_welcomemsg_role(self,mocker):
        mocker.patch('main_menu.user_has_permissions',lambda x : x)
        MainMenu.welcomemsg_role()
