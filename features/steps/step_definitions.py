from lib2to3.fixes.fix_input import context
from behave import *
import requests
from utilities.configurations import *
from utilities.payload_manager import *
from utilities.utils import *
from utilities.resources import *
import json

# @smoke @post @create 
@given('Create booking payload to create new booking')
def create_booking_payload(context):
    context.url = getConfig()['API']['base_url']+ApiResources.create_booking
    context.json = create_bookingPayload(firstname="Suresh", lastname="Abo", totalprice=123, depositpaid=False, additionalneeds=["Breakfast", "Lunch"])
    context.headers = Utils().common_headers()

@when('we execute the Post request')
def execute_payload(context):
    context.response = requests.post(url=context.url, json=context.json, headers=context.headers)
    #print(context.response)

@then('new booking is created')
def verify_bookingid(context):
    #print(context.response.text)
    context.response_json = context.response.json()
    #print(type(context.response_json))
    context.booking_Id = context.response_json['bookingid']
    #print(context.booking_Id)
    assert context.response.status_code == 200

#@regression @get @random_bookingid
@given('A booking id and payload')
def step_bookid(context):
    #print(context.random_bookingid)
    context.bookingid = context.random_bookingid
    context.url = getConfig()['API']['base_url'] + ApiResources.get_single_booking + str(context.bookingid)
    context.headers = Utils().common_headers()

@when('we execute the get request')
def step_execute(context):
    context.response = requests.get(url=context.url, headers=context.headers)
    #print(context.response)

@then('booking details are retrieved')
def verify_booking_response(context):
    assert context.response.status_code == 200
    assert context.response.json()['firstname'] != ""
    assert context.response.json()['lastname'] != ""

# @regression @getall
@given('details to get all bookings')
def step_allBookId(context):
    context.url = getConfig()['API']['base_url'] + ApiResources.get_all_bookings
    # context.headers = Utils().common_headers()

@when('get request without booingid is executed')
def step_getAll_execute(context):
    context.response = requests.get(url=context.url)

@then('bookings details are retrieved in a list')
def verify_booking_response(context):
    assert context.response.status_code == 200
    #assert "OK" in context.response
    #assert isinstance((context.response.json()), list)
    assert type(context.response.json()) == list

#@regression @deleted @create_token @create_bookingid
@given('API details for delete request')
def delete_request_details(context):
    #print(context.booking_id)
    context.url = getConfig()['API']['base_url']+ApiResources.delete+str(context.booking_id)
    context.headers = Utils().common_headers()
    context.cookie = {'token': context.token}

@when('delete request is executed')
def execute_delete_request(context):
    context.response = requests.delete(url=context.url, headers=context.headers, cookies=context.cookie)
    #print(context.response)

@Then('verify delete response')
def verify_delete_response(context):
    assert context.response.status_code == 201
    #assert "Created" in context.response

#@integration @tc1 @partialupdate @create_token @create_bookingid @patch
@given('API details for partial update request')
def update_request_details_step(context):
    #print(context.booking_id)
    #print(context.token)
    context.url = getConfig()['API']['base_url']+ApiResources.update+str(context.booking_id)
    context.json = payload_patch_test("firsttest", "lasttest")
    context.header = Utils().common_headers()
    context.cookie = {'token': context.token}

@when('patch request is executed')
def update_request_execution(context):
    context.response = requests.patch(url=context.url, json=context.json, headers=context.header, cookies=context.cookie)
    #print(context.response)

@then('verify updated data from response')
def verify_update_request_response(context):
    assert context.response.status_code == 200
    assert context.response.json()['firstname'] == "firsttest"
    assert context.response.json()['lastname'] == "lasttest"

# @regression @fullupdate @create_token @create_bookingid @put
@given('API details for full update request')
def put_request_details_step(context):
    #print(context.booking_id)
    #print(context.token)
    context.url = getConfig()['API']['base_url']+ApiResources.update+str(context.booking_id)
    context.json = payload_update()
    context.header = Utils().common_headers_with_cookie(context.token)


@when('put request is executed')
def put_request_execution(context):
    context.response = requests.put(url=context.url, json=context.json, headers=context.header)
    #print(context.response)


@then('verify updated full data from response')
def verify_put_request_response(context):
    assert context.response.status_code == 200
    assert context.response.json()['firstname'] == "testfirst"
    assert context.response.json()['lastname'] == "testlast"
    assert context.response.json()['totalprice'] == 330

# @integration @tc2 @create_token @create_bookingid
@given('API details for create and delete integration')
def delete_request_details(context):
    #print(context.booking_id)
    context.url = getConfig()['API']['base_url']+ApiResources.delete+str(context.booking_id)
    context.headers = Utils().common_headers()
    context.cookie = {'token': context.token}

@when('delete request is executed on created booking_id')
def execute_delete_request(context):
    context.response = requests.delete(url=context.url, headers=context.headers, cookies=context.cookie)
    #print(context.response)

@Then('verify that delete Operation is suucessful')
def verify_delete_response(context):
    assert context.response.status_code == 201
    #assert "Created" in context.response

@Then('verify updated get Operation throws 404 error')
def verify_get_on_deleted_id(context):
    context.url = getConfig()['API']['base_url'] + ApiResources.get_single_booking + str(context.booking_id)
    #print(context.url)
    context.headers = Utils().common_headers()
    context.get_response = requests.get(url=context.url, headers=context.headers)
    #print(context.get_response)
    #print(context.get_response.status_code)
    assert context.get_response.status_code != 200

# @integration @tc3 @create_token @create_bookingid 
@given('API details for create and update integration')
def put_request_details(context):
    #print(context.booking_id)
    context.url = getConfig()['API']['base_url']+ApiResources.delete+str(context.booking_id)
    context.headers = Utils().common_headers()
    context.cookie = {'token': context.token}
    context.json = payload_update()

@when('update request is executed on created booking_id')
def execute_put_request(context):
    context.response = requests.put(url=context.url, headers=context.headers, cookies=context.cookie, json=context.json)
    #print(context.response.json())

@Then('verify that put Operation is suucessful')
def verify_put_response(context):
    assert context.response.status_code == 200
    assert context.response.json()['firstname'] == "testfirst"
    assert context.response.json()['lastname'] == "testlast"
    assert context.response.json()['totalprice'] == 330

@Then('verify updated data with get Operation')
def verify_get_on_updated_id(context):
    context.url = getConfig()['API']['base_url'] + ApiResources.get_single_booking + str(context.booking_id)
    #print(context.url)
    context.headers = Utils().common_headers()
    context.get_response = requests.get(url=context.url, headers=context.headers)
    #print(context.get_response)
    #print(context.get_response.status_code)
    assert context.get_response.status_code == 200
    assert context.response.json()['firstname'] == "testfirst"
    assert context.response.json()['lastname'] == "testlast"
    assert context.response.json()['totalprice'] == 330

# @integration @tc4 @create_token @create_bookingid 
@given('API details for deleting a newly created bookingid')
def delete_request_details(context):
    #print(context.booking_id)
    context.url = getConfig()['API']['base_url']+ApiResources.delete+str(context.booking_id)
    context.headers = Utils().common_headers()
    context.cookie = {'token': context.token}

@when('delete request is executed on newly created booingid')
def execute_delete_request(context):
    context.response = requests.delete(url=context.url, headers=context.headers, cookies=context.cookie)
    #print(context.response)

@Then('verify delete response status_code and response_time')
def verify_put_response(context):
    assert context.response.status_code == 201
    assert context.response.elapsed.total_seconds() <= 200

# @negative @create @tc5
@given('Create booking with Invalid payload')
def create_booking_invalid_payload(context):
    context.url = getConfig()['API']['base_url']+ApiResources.create_booking
    context.json = {}
    context.headers = Utils().common_headers()

@when('Post request is executed wit Invalid payload')
def execute_payload(context):
    context.response = requests.post(url=context.url, json=context.json, headers=context.headers)
    #print(context.response)

@then('new booking is not created and system responds with status_code 500')
def verify_bookingid(context):
    #print(context.response.text)
    #context.response_json = context.response.json()
    #print(type(context.response_json))
    #context.booking_Id = context.response_json['bookingid']
    #print(context.booking_Id)
    assert context.response.status_code == 500

# @integration @tc6 @create_token @create_bookingid 
@given('API details for create and delete integration to update')
def delete_request_details(context):
    #print(context.booking_id)
    context.url = getConfig()['API']['base_url']+ApiResources.delete+str(context.booking_id)
    context.headers = Utils().common_headers()
    context.cookie = {'token': context.token}

@when('delete operation is executed on created booking_id')
def execute_delete_request(context):
    context.response = requests.delete(url=context.url, headers=context.headers, cookies=context.cookie)
    #print(context.response)

@Then('verify that delete Operation is sucessful with 201 status_code')
def verify_delete_response(context):
    assert context.response.status_code == 201
    #print(context.response)
    # assert "Created" in context.response.json()

@Then('verify that patch Operation to update throws 405 error')
def verify_patch_on_deleted_id(context):
    context.url = getConfig()['API']['base_url'] + ApiResources.update + str(context.booking_id)
    #print(context.url)
    context.headers = Utils().common_headers()
    context.json = payload_patch_test("namefirst", "namelast")
    context.get_response = requests.get(url=context.url, headers=context.headers, json=context.json, cookies=context.cookie)
    #print(context.get_response)
    #print(context.get_response.status_code)
    assert context.get_response.status_code == 404