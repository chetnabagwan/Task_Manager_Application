import pytest
from db.database_functions import create_table,add_data,fetch_user,display_data,update_data,fetch_data
from db.database_connection import DatabaseContextManager

data = ('example', 'data')
mock_fetchall_result = [('result1',), ('result2',)]
mock_fetchone_result = ('result1',)

@pytest.fixture()
def mock_db_connection(mocker):
    '''Test Fixture to mock db connection'''

    mock_connection = mocker.MagicMock(spec=DatabaseContextManager)
    mocker.patch('db.database_functions.DatabaseContextManager', return_value=mock_connection)
    mock_cursor = mocker.MagicMock()
    mock_connection.__enter__.return_value.cursor.return_value = mock_cursor

    return mock_cursor

def test_create_table(mock_db_connection):
    create_table('test')

def test_add_date(mock_db_connection):
    add_data('test')

def test_fetch_user(mock_db_connection):
    mock_cursor =mock_db_connection
    mock_cursor.fetchone.return_value = mock_fetchone_result
    fetch_user('test','chetna','che123')

def test_display_data(mock_db_connection):
    mock_cursor = mock_db_connection
    mock_cursor.fetchall.return_value = mock_fetchall_result
    display_data('test')

def test_update_data(mock_db_connection):
    update_data('test')

def test_fetch_data(mock_db_connection):
    mock_cursor = mock_db_connection
    mock_cursor.fetchall.return_value = mock_fetchall_result
    fetch_data('test')

