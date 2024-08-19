import pytest
import requests


@pytest.fixture()
def login():
    body = {
        "username": "admin",
        "password": "password123"
    }

    headers = {'Content-Type': 'application/json'}
    response = requests.post(
         'https://restful-booker.herokuapp.com/auth',
         json=body,
         headers=headers
    )
    assert response.status_code == 200, f'Expected Status Code 200,but got {response.status_code}'
    yield response.json()['token']


@pytest.fixture(scope='session')
def create_booking_id():
    data = {
        "firstname": "Anna",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(
        'https://restful-booker.herokuapp.com/booking',
        json=data,
        headers=headers
    )

    assert response.status_code == 200, f'Expected Status Code 200,but got {response.status_code}'

    response_data = response.json()
    assert "bookingid" in response_data, "The response does not contain 'bookingid'"
    yield response_data['bookingid']
