import pytest
import sqlite3

from db.database_connection import DatabaseContextManager

class TestDatabaseConnection:
    def test_db_connection_context_manager(self,mocker):
        '''Test function to test db connection context manager success'''

        mock_connect = mocker.patch('sqlite3.connect')
        mock_connection = mocker.MagicMock()
        mock_connect.return_value = mock_connection

        with DatabaseContextManager('data.db') as conn:
            assert conn is mock_connection
            assert mock_connect.call_count == 1

        # After exiting the context manager
        mock_connection.commit.assert_called_once()
        mock_connection.close.assert_called_once()

    def test_db_connection_context_manager_error(self, mocker):
        '''Test function to test db connection context manager error'''

        mock_connect = mocker.patch('sqlite3.connect')
        mock_connection = mocker.MagicMock(spec=sqlite3.Connection)
        mock_connect.return_value = mock_connection

        with pytest.raises(sqlite3.Error):
            with DatabaseContextManager('data.db'):
                raise sqlite3.Error('Some error')

        # After exiting the context manager with an exception
        mock_connection.commit.assert_not_called()
        mock_connection.close.assert_called_once()