

def create_bookingPayload(firstname, lastname, totalprice, depositpaid, additionalneeds):
    body = {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": {
            "checkin": "2023-08-04",
            "checkout": "2023-08-11"
        },
        "additionalneeds": additionalneeds
    }
    return body

def create_token_payload():
    body = {
    "username" : "admin",
    "password" : "password123"
    }
    return body

def payload_patch_test(firstname, lastname):
    payload = {
        "firstname" : firstname,
        "lastname" : lastname
    }
    return payload

def payload_update():
    payload = {
        "firstname": "testfirst",
        "lastname": "testlast",
        "totalprice": 330,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-05",
            "checkout": "2023-02-01"
        },
        "additionalneeds": "Snacks"
    }
    return payload
    