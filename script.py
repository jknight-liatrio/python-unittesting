import requests


def sum(a, b):
    return a+b


def do_something_with_alert(alert_data):
    # external request with alert data
    print('foo')
    return 'foo'


def get_weather_events(state):
    try:
        alerts = requests.get(f"https://api.weather.gov/alerts/active?area={state}")
        for alert in alerts:
            result = do_something_with_alert(alert)
            print('result')
        pass
    except requests.exceptions.HTTPError as e:
        pass

    return alerts


