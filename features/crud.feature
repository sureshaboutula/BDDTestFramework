Feature: Verify CRUD Operations for RestFull Booker API
  # Enter feature description here

  @smoke @post @create
  Scenario: Verify the create booking status and booking id should not be null
    Given Create booking payload to create new booking
    When we execute the Post request
    Then new booking is created

  @regression @get @random_bookingid
  Scenario: Verify the booking details for an existing bookingid
    Given A booking id and payload
    When we execute the get request
    Then booking details are retrieved

  @regression @getall
  Scenario: Get all bookings in a list
    Given details to get all bookings
    When get request without booingid is executed
    Then bookings details are retrieved in a list

  @regression @deleted @create_token @create_bookingid
  Scenario: Verify API response for delete Operations
    Given API details for delete request
    When delete request is executed 
    Then verify delete response

  @integration @tc1 @partialupdate @create_token @create_bookingid @patch
  Scenario: TC1 # Verify API response for partial update Operation
    Given API details for partial update request
    When patch request is executed
    Then verify updated data from response

  @regression @fullupdate @create_token @create_bookingid @put
  Scenario: Verify API response for full update Operation
    Given API details for full update request
    When put request is executed
    Then verify updated full data from response

  @integration @tc2 @create_token @create_bookingid 
  Scenario: TC2 # Create a Booking, Delete the Booking with ID and Verify using GET request that it should not exist.
    Given API details for create and delete integration
    When delete request is executed on created booking_id
    Then verify that delete Operation is suucessful
    And verify updated get Operation throws 404 error

  @integration @tc3 @create_token @create_bookingid 
  Scenario: TC3 # Trying to GET details of an Updated Request
    Given API details for create and update integration
    When update request is executed on created booking_id
    Then verify that put Operation is suucessful
    And verify updated data with get Operation
  
  @integration @tc4 @create_token @create_bookingid 
  Scenario: TC4 # Trying to Delete a newly created booking
    Given API details for deleting a newly created bookingid
    When delete request is executed on newly created booingid
    Then verify delete response status_code and response_time
  
  @negative @create @tc5
  Scenario: TC5 # Trying to Verify Create a booking with Invalid or empty payload
    Given Create booking with Invalid payload
    When Post request is executed wit Invalid payload
    Then new booking is not created and system responds with status_code 500
  
  @integration @tc6 @create_token @create_bookingid 
  Scenario: TC6 # Trying to Update on a Delete Id
    Given API details for create and delete integration to update 
    When delete operation is executed on created booking_id
    Then verify that delete Operation is sucessful with 201 status_code
    And verify that patch Operation to update throws 405 error



  



