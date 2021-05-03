import requests
from py.xml import html


def test_1_success():
    request = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=6ISQW3Z84MLEBQI5"
    resp = requests.get(request)
    print("Request:\n" + request)
    print(resp)
    print("Response: \n" + str(resp.content))
    assert (resp.status_code == 200)


def test_2_404_invalid_value():
    request = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM123&apikey=6ISQW3Z84MLEBQI5"
    resp = requests.get(request)
    print("Request:\n" + request)
    print(resp)
    print("Response: \n" + str(resp.content))

    assert (resp.status_code == 404)


def test_3_400_invalid_key():
    request = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol123=IBM&apikey=6ISQW3Z84MLEBQI5"
    resp = requests.get(request)
    print("Request:\n" + request)
    print(resp)
    print("Response: \n" + str(resp.content))
    assert (resp.status_code == 400)


def test_4_400_missing_required_key():
    request = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&apikey=6ISQW3Z84MLEBQI5"
    resp = requests.get(request)
    print("Request:\n" + request)
    print(resp)
    print("Response: \n" + str(resp.content))
    assert (resp.status_code == 400)


def test_5_403_apikey_authentication():
    request = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&apikey=---------"
    resp = requests.get(request)
    print("Request:\n" + request)
    print(resp)
    print("Response: \n" + str(resp.content))
    assert (resp.status_code == 403)


def test_6_403_apikey_authentication():
    request = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&apikey="
    resp = requests.get(request)
    print("Request:\n" + request)
    print(resp)
    print("Response: \n" + str(resp.content))
    assert (resp.status_code == 403)


def test_7_403_apikey_authentication():
    request = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&apikey=---------"
    resp = requests.get(request)
    print("Request:\n" + request)
    print(resp)
    print("Response: \n" + str(resp.content))
    assert (resp.status_code == 403)
