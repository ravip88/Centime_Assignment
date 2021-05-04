import requests
from py.xml import html
import time

def test_1_invalid_throttling_limit_message_validation():
    resp=str()
    for _ in range(6):
        request = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&apikey=---------"
        resp = requests.get(request)
        print("Request:\n" + request)
        print(resp)
        print("Response: \n" + str(resp.content))
    assert (resp.content.decode('utf-8') == '{\n    "Note": "Thank you for using Alpha Vantage! Our standard API call frequency is 5 calls per minute and 500 calls per day. Please visit https://www.alphavantage.co/premium/ if you would like to target a higher API call frequency."\n}')

def test_2_valid_throttling_limit_message_validation():
    time.sleep(60)
    resp=str()
    for _ in range(4):
        request = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&apikey=---------"
        resp = requests.get(request)
        print("Request:\n" + request)
        print(resp)
        print("Response: \n" + str(resp.content))
    assert (resp.content.decode('utf-8') != '{\n    "Note": "Thank you for using Alpha Vantage! Our standard API call frequency is 5 calls per minute and 500 calls per day. Please visit https://www.alphavantage.co/premium/ if you would like to target a higher API call frequency."\n}')


def test_3_valid_request_success():
    time.sleep(60)
    request = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=6ISQW3Z84MLEBQI5"
    resp = requests.get(request)
    print("Request:\n" + request)
    print(resp)
    print("Response: \n" + str(resp.content))
    assert (resp.status_code == 200)


def test_4_404_invalid_value():
    request = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM123&apikey=6ISQW3Z84MLEBQI5"
    resp = requests.get(request)
    print("Request:\n" + request)
    print(resp)
    print("Response: \n" + str(resp.content))

    assert (resp.status_code == 404)


def test_5_400_invalid_key():
    request = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol123=IBM&apikey=6ISQW3Z84MLEBQI5"
    resp = requests.get(request)
    print("Request:\n" + request)
    print(resp)
    print("Response: \n" + str(resp.content))
    assert (resp.status_code == 400)


def test_6_400_missing_required_key():
    request = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&apikey=6ISQW3Z84MLEBQI5"
    resp = requests.get(request)
    print("Request:\n" + request)
    print(resp)
    print("Response: \n" + str(resp.content))
    assert (resp.status_code == 400)


def test_7_403_invalid_apikey_authentication():
    request = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&apikey=---------"
    resp = requests.get(request)
    print("Request:\n" + request)
    print(resp)
    print("Response: \n" + str(resp.content))
    assert (resp.status_code == 403)


def test_8_403_missing_apikey_authentication():
    request = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&apikey="
    resp = requests.get(request)
    print("Request:\n" + request)
    print(resp)
    print("Response: \n" + str(resp.content))
    assert (resp.status_code == 403)
