import pytest
from src.utils.config import Config


@pytest.fixture(scope='session',autouse=True)
@Config.config_loader
def my_config_loader():
    # print(Config.TODAY)
    pass