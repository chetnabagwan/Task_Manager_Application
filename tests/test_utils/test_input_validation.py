"""Test file for Input_validation.py"""

import pytest
from datetime import datetime
from src.utils.config import Config
from src.utils.helper_functions import parse_date,format_date
from src.utils.input_validation import InputValidations

#@pytest.mark.usefixtures('my_config_loader')
class TestUtils:

    @pytest.mark.parametrize("password, expected_result", [
        ("Che@12", True),
        ("chetna", False),
        ("Tan@13", True),
        ("Raj$2a",True)])
    def test_password_validator(self,password, expected_result):
        # Call the method under test
        result = InputValidations.password_validator(password)
        # Assert the result
        assert result == expected_result
    
    @pytest.mark.parametrize("input_value, expected_result", [
        ("abc ", False),
        (" ", False),
        ("Hello", True),
        ("my name is john",True)])
    def test_gen_validator(self,input_value, expected_result):
        result = InputValidations.gen_validator(input_value)
        assert result == expected_result
    
    @pytest.mark.parametrize("user_input, expected_output, is_invalid_input", [
        ("Learn python", "Learn python", False),
        (" ", Config.INVALID_INPUT, True),
        ("python", "python", False)
    ])
    def test_task_name_validator(self,monkeypatch, capsys, user_input, expected_output, is_invalid_input):
        # Mock input and gen_validator
        monkeypatch.setattr('builtins.input', lambda _: user_input)
        monkeypatch.setattr('src.utils.input_validation.InputValidations.gen_validator', lambda x: is_invalid_input)

        result = InputValidations.task_name_validator()

        captured = capsys.readouterr()  # Capture printed output
        #assert result == expected_output
        if not is_invalid_input:
            assert Config.INVALID_INPUT in captured.out  # Check if the error message is printed when needed
        else:
            assert not captured.out
    
    @pytest.mark.parametrize("user_input, expected_output, is_invalid_input", [
        ("Learn python", "Learn python", False),
        (" ", Config.INVALID_INPUT, True),
        ("python", "python", False)
    ])
    def test_task_desc_validator(self,monkeypatch, capsys, user_input, expected_output, is_invalid_input):
        # Mock input and gen_validator
        monkeypatch.setattr('builtins.input', lambda _: user_input)
        monkeypatch.setattr('src.utils.input_validation.InputValidations.gen_validator', lambda x: is_invalid_input)

        result = InputValidations.task_desc_validator()

        captured = capsys.readouterr()
        
        if not is_invalid_input:
            assert Config.INVALID_INPUT in captured.out  # Check if the error message is printed when needed
        else:
            assert not captured.out
            
    
    def parse_date(date_str, fmt):
        return datetime.strptime(date_str, fmt)

    def format_date(date_obj, fmt):
        return date_obj.strftime(fmt)
    
    @pytest.mark.parametrize("user_input, today_date, expected_output, is_valid_input", [
        ("01-01-2023", "01-01-2023", "01-01-2023", True),  # Valid input
        ("01-01-2022", "01-01-2023", Config.INVALID_DUE_DATE, False),   # Invalid input
        ("10-01-2023", "01-01-2023", "01-01-2023", True) ])
    def test_date_validator(self,monkeypatch, capsys, user_input, today_date,expected_output, is_valid_input):
    
        monkeypatch.setattr('builtins.input', lambda _: user_input)
        monkeypatch.setattr('src.utils.helper_functions.parse_date', parse_date)
        monkeypatch.setattr('src.utils.helper_functions.format_date', format_date)
        result = InputValidations.date_validator("user_id_placeholder", today_date)

        captured = capsys.readouterr()  # Capture printed output
        #assert result == expected_output         
        if not is_valid_input:
            assert Config.INVALID_DUE_DATE in captured.out  # Check if the error message is printed when needed
        else:
            assert not captured.out

    @pytest.mark.parametrize(("user_input, expected_category"), [
        (("1",), "Today"),
        (("2",), "Important"),
        (("4", "3"), "For later"), 
        (("3",), "For later")])
    def test_task_category_validator(self,monkeypatch, user_input, expected_category):
        user_input_iter = iter(user_input)
        monkeypatch.setattr('builtins.input', lambda _: next(user_input_iter))
        result = InputValidations.task_category_validator()
        
        assert result == expected_category
      
    @pytest.mark.parametrize(("user_input, expected_output"), [
        (("1028",), "1028"),
        (("8932",), "8932"),
        (("12", "2534"), "2534"), 
        (("5239",),"5239" )])
    def test_userid_validator(self,monkeypatch,user_input,expected_output):
        user_input_iter = iter(user_input)
        monkeypatch.setattr('builtins.input', lambda _: next(user_input_iter))
        result = InputValidations.userid_validator()
        assert result == expected_output

    @pytest.mark.parametrize(("user_input, expected_output"), [
    (("1028",), "1028"),
    (("8932",), "8932"),
    (("1292732", "2534"), "2534"), 
    (("5239",),"5239" )])
    def test_taskid_validator(self,monkeypatch,user_input,expected_output):
        user_input_iter = iter(user_input)
        monkeypatch.setattr('builtins.input', lambda _: next(user_input_iter))
        result = InputValidations.taskid_validator()
        assert result == expected_output


    @pytest.mark.parametrize(("user_input, expected_status"), [
    (("0",), "Reassigned"),
    (("3", "1"), "Completed"), 
    (("0",),"Reassigned")])
    def test_task_status_validator(self,monkeypatch, user_input, expected_status):
        user_input_iter = iter(user_input)
        monkeypatch.setattr('builtins.input', lambda _: next(user_input_iter))
        result = InputValidations.task_status_validator()
        assert result == expected_status