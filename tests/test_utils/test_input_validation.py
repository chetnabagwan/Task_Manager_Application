import pytest
from src.utils.input_validation import password_validation,username_validator

class TestUtils:

    def test_password_is_validated(self):
       assert password_validation('Tan@12')  

    def test_password_isnot_validated(self):
       assert not password_validation('12abj')
  
    def test_username_is_validated(self):
        assert username_validator('chEtna')

    def test_username_isnot_validated(self):
        r = username_validator('ch1@6nA')
        assert r is False


    