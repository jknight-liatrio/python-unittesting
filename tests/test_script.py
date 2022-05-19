import pytest
import requests
from unittest import mock
from unittest.mock import MagicMock, Mock
from script import sum, get_weather_events, do_something_with_alert


def test_sum():
    assert sum(1, 1) == 2


def test_get_weather_events_404():

    def mock_fucntion():
        raise requests.exceptions.HTTPError('404')


    with mock.patch('requests.get') as mock_request:

        mock_result = MagicMock()

        mock_result.raise_for_status = mock_fucntion

        mock_request.return_value = mock_result
        get_weather_events('TX')
        mock_request.assert_called()


def test_get_weather_events_with_alerts():
    alert_called = 0

    def mock_do_something_function(alert):
        nonlocal alert_called
        alert_called += 1
        return 'foo'

    def mock_request_function():
        pass


    with mock.patch('requests.get') as mock_request, \
            mock.patch('script.do_something_with_alert') as mock_do_something:
        mock_result = MagicMock()

        mock_do_something.side_effect = mock_do_something_function

        mock_result.raise_for_status = mock_request_function

        mock_request.return_value = ['alert1', 'alert2']
        get_weather_events('TX')
        mock_request.assert_called()
    assert alert_called == 2



@pytest.mark.integration
def test_get_weather_events_functional():
    result = get_weather_events('TX')
    assert result.status_code == 200
