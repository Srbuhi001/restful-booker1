import pytest
import requests
import allure

import test_1_booking_token
import test_2_booking_post


@allure.feature('Booking Feature')
@allure.suite('Partial Update Booking Suite')
@allure.title('Test Partial Update Booking')
@allure.description('Test to partially update a booking and verify the response.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_partial_update_booking():
    body = {
        "firstname": "James",
        "lastname": "Brown"
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': f'token={test_1_booking_token.my_token}'
    }

    with allure.step('Send PATCH request to partially update the booking'):
        response = requests.patch(
            f'https://restful-booker.herokuapp.com/booking/{test_2_booking_post.my_bookingid}',
            json=body,
            headers=headers
        )

    with allure.step('Verify the status code is 200'):
        assert response.status_code == 200, f'Expected status code 200 but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify the firstname is updated'):
        assert body['firstname'] == response_data['firstname'], f"Expected firstname to be {body['firstname']} but got {response_data['firstname']}"

    with allure.step('Verify the lastname is updated'):
        assert body['lastname'] == response_data['lastname'], f"Expected lastname to be {body['lastname']} but got {response_data['lastname']}"

    with allure.step('Verify the original booking details are still present'):
        assert 'totalprice' in response_data, 'Totalprice field is missing in the response'
        assert 'depositpaid' in response_data, 'Depositpaid field is missing in the response'
        assert 'bookingdates' in response_data, 'Bookingdates field is missing in the response'
        assert 'checkin' in response_data['bookingdates'], 'Checkin date is missing in the bookingdates'
        assert 'checkout' in response_data['bookingdates'], 'Checkout date is missing in the bookingdates'
        assert 'additionalneeds' in response_data, 'Additionalneeds field is missing in the response'

    with allure.step('Printing response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)



@allure.feature('Booking Feature')
@allure.suite('Negative Partial Update Suite')
@allure.title('Negative Partial Update Booking with Invalid Token')
@allure.description('This test attempts to partially update a booking using an invalid token and verifies the failure.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_negative_partial_update_booking():
    body = {
        "firstname": "James",
        "lastname": "Brown"
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': f'token=12345asd'
    }

    with allure.step('Send PATCH request with invalid token'):
        response = requests.patch(
            f'https://restful-booker.herokuapp.com/booking/{test_2_booking_post.my_bookingid}',
            json=body,
            headers=headers
        )

    with allure.step('Verify the status code is 403'):
        assert response.status_code == 403, f'Expected status code 403 but got {response.status_code}'


@allure.feature('Booking Feature')
@allure.suite('Negative Partial Update Suite')
@allure.title('Negative Partial Update Booking with Missing Token')
@allure.description('This test attempts to partially update a booking without a token and verifies the failure.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_negative_partial_update_with_invalid_token_booking():
    body = {
        "firstname": "James",
        "lastname": "Brown"
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    with allure.step('Send PATCH request without token'):
        response = requests.patch(
            f'https://restful-booker.herokuapp.com/booking/{test_2_booking_post.my_bookingid}',
            json=body,
            headers=headers
        )

    with allure.step('Verify the status code is 403'):
        assert response.status_code == 403, f'Expected status code 403 but got {response.status_code}'
