import requests
import pytest
import allure

import test_1_booking_token
import test_2_booking_post


@allure.feature('Booking Feature')
@allure.suite('Booking Deletion Suite')
@allure.title('Delete Booking by ID')
@allure.description('This test deletes a booking by its ID and verifies that the deletion was successful.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_delete_booking_by_id():
    headers = {'Content-Type': 'application/json', 'Cookie': f'token={test_1_booking_token.my_token}'}

    with allure.step('Send DELETE request to remove the booking by ID'):
        response = requests.delete(
            f'https://restful-booker.herokuapp.com/booking/{test_2_booking_post.my_bookingid}',
            headers=headers
        )

    with allure.step('Verify the status code is 201 for successful deletion'):
        assert response.status_code == 201, f'Expected status code 201 but got {response.status_code}'
