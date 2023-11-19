import pytest
from unittest import mock
from authentication import authenticate_user

def test_authenticate_user_success():
    mock_response = mock.Mock()
    mock_response.status_code = 200

    with mock.patch('requests.post') as mock_post:
        mock_post.return_value = mock_response


        assert authenticate_user('user123', 'password123') is True


        mock_post.assert_called_once_with('https://api.example.com/auth', json={'username': 'user123', 'password': 'password123'})

def test_authenticate_user_failure():
    mock_response = mock.Mock()
    mock_response.status_code = 401

    with mock.patch('requests.post') as mock_post:
        mock_post.return_value = mock_response


        assert authenticate_user('invalid_user', 'invalid_password') is False


        mock_post.assert_called_once_with('https://api.example.com/auth', json={'username': 'invalid_user', 'password': 'invalid_password'})

if __name__ == "__main__":
    pytest.main()