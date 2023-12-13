"""Test file for app.py"""
from utils.config import Config
from app import app

def test_app(mocker,capsys,caplog):
    """Test function to test app function"""
    mocker.patch('app.Config.config_loader',lambda x:x)
    mocker.patch('app.create_table')
    mocker.patch('app.MainMenu.start')
    app()
    captured = capsys.readouterr()
    assert Config.WELCOME_MESSAGE in captured.out
    assert 'Application started' in caplog.text
    assert 'Application ended' in caplog.text
    

