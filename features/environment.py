import requests
import json
from behave import *
import random

from utilities.resources import *
from utilities.configurations import *
from utilities.utils import *
from utilities.payload_manager import *

def before_scenario(context, scenario):
    if "create_token" in scenario.tags:
        token_response = requests.post(
            url=getConfig()['API']['base_url']+ApiResources.token,
            headers= Utils().common_headers(),
            json= create_token_payload()
        )
        context.token = token_response.json()["token"]

    if "create_bookingid" in scenario.tags:
        new_booking = requests.post(
            url = getConfig()['API']['base_url']+ApiResources.create_booking,
            json = create_bookingPayload(firstname="Ramesh", lastname="Abo", totalprice=143, depositpaid=True, additionalneeds="Lunch"),
            headers = Utils().common_headers()
        )
        context.booking_id = new_booking.json()['bookingid']
    
    if "random_bookingid" in scenario.tags:
        getall_bookings = requests.get(
            url = getConfig()['API']['base_url'] + ApiResources.get_all_bookings
        )
        len_bookingids = len(getall_bookings.json())
        #context.random_bookingid = random.randint(0, len_bookingids)
        context.random_bookingid = random.choice(getall_bookings.json())['bookingid']