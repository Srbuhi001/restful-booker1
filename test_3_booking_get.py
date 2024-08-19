import allure
import pytest
import requests

import test_2_booking_post


@allure.feature('Booking Feature')
@allure.suite('GET Booking Suite')
@allure.title('Test getting all bookings')
@allure.description('This test retrieves all bookings and checks the response status and content .')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_get_booking_all():
    with allure.step('Send request to get all bookings'):
        response = requests.get('https://restful-booker.herokuapp.com/booking')

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    with allure.step('Verify the response contains a non-empty list'):
        assert len(response.json()) > 0, 'The list  should not be empty'


@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('GET Booking Suite')
@allure.title('Test getting  booking by ID')
@allure.description('This test retrieves a bookings by ID and checks the response status and content')
@allure.severity(allure.severity_level.NORMAL)
def test_get_booking_by_id():
    with allure.step('Send GET request to retrieve booking by ID'):
        response = requests.get(f'https://restful-booker.herokuapp.com/booking/{test_2_booking_post.my_bookingid}')

    with allure.step('Verify the status code is 200'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response contains the "firstname" field'):
        assert 'firstname' in response_data, "The response does not contain 'firstname'"

    with allure.step('Verify response contains the "lastname" field'):
        assert 'lastname' in response_data, "The response does not contain 'lastname'"

    with allure.step('Verify response contains the "totalprice" field'):
        assert 'totalprice' in response_data, "The response does not contain 'totalprice'"

    with allure.step('Verify response contains the "depositpaid" field'):
        assert 'depositpaid' in response_data, "The response does not contain 'depositpaid'"

    with allure.step('Verify response contains the "bookingdates" field'):
        assert 'bookingdates' in response_data, "The response does not contain 'bookingdates'"

    with allure.step('Verify "bookingdates" contains the "checkin" field'):
        assert 'checkin' in response_data['bookingdates'], "The response does not contain 'checkin'"

    with allure.step('Verify "bookingdates" contains the "checkout" field'):
        assert 'checkout' in response_data['bookingdates'], "The response does not contain 'checkout'"

    with allure.step('Verify response contains the "additionalneeds" field'):
        assert 'additionalneeds' in response_data, "The response does not contain 'additionalneeds'"

    with allure.step('Verify "depositpaid" is either True or False'):
        assert response_data['depositpaid'] is True or response_data['depositpaid'] is False, 'ERROR depositpaid'

    with allure.step('Verify "totalprice" is an integer or float'):
        assert isinstance(response_data['totalprice'], (int, float)), 'ERROR: totalprice is neither an int nor a float'

    with allure.step('Printing response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)