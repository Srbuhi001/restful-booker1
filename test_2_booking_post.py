import allure
import pytest
import requests

my_bookingid = 0


@allure.feature('Booking Feature')
@allure.suite('Create Booking Suite')
@allure.title('Test Create Booking')
@allure.description('Test to create a booking and verify the response .')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_create_booking():
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

    with allure.step('Send POST request to create a booking'):
        response = requests.post(
            'https://restful-booker.herokuapp.com/booking',
            json=data,
            headers=headers
        )

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify the response contains "bookingid"'):
        assert "bookingid" in response_data, "The response does not contain 'bookingid'"

    with allure.step('Verify the response contains "booking"'):
        assert "booking" in response_data, "The response does not contain 'booking'"

    response_booking = response_data['booking']

    with allure.step('Verify  "firstname" is correct'):
        assert 'firstname' in response_booking, "'firstname' key not found in response"
        assert response_booking['firstname'] == data['firstname'], f"Expected firstname  but got'{response_booking['firstname']}'"

    with allure.step('Verify  "lastname" is correct'):
        assert 'lastname' in response_booking, "'lastname' key not found in response"
        assert response_booking['lastname'] == data['lastname'], f"Expected lastname  but got '{response_booking['lastname']}'"

    with allure.step('Verify  "totalprice" is correct'):
        assert 'totalprice' in response_booking, "'totalprice' key not found in response"
        assert response_booking['totalprice'] == data['totalprice'], f"Expected totalprice but got '{response_booking['totalprice']}'"

    with allure.step('Verify "depositpaid" is correct'):
        assert 'depositpaid' in response_booking, "'depositpaid' key not found in response"
        assert response_booking['depositpaid'] == data['depositpaid'], f"Expected depositpaid  but got '{response_booking['depositpaid']}'"

    with allure.step('Verify the response contains "bookingdates" with correct checkin and checkout dates'):
        assert 'bookingdates' in response_booking, "'bookingdates' key not found in response"
        assert response_booking['bookingdates']['checkin'] == data['bookingdates']['checkin'], f"Expected checkin to be {data['bookingdates']['checkin']} but got '{response_booking['bookingdates']['checkin']}'"
        assert response_booking['bookingdates']['checkout'] == data['bookingdates']['checkout'], f"Expected checkout, but got '{response_booking['bookingdates']['checkout']}'"
    with allure.step('Verify the response contains "additionalneeds" and it matches the input'):
        assert 'additionalneeds' in response_booking, "'additionalneeds' key not found in response"
        assert response_booking['additionalneeds'] == data['additionalneeds'], f"Expected additionalneeds , but got '{response_booking['additionalneeds']}'"

    global my_bookingid
    my_bookingid = response_data['bookingid']
