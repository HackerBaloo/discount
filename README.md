# Discount

## What is it?
A microservice to to handle all about discount codes.

## API
Currently the dicount service has two endpoints.
The API is asynchrounious. The response will come as either a 'user' or 'administrative' event


1. GET https://url/discount-code/<string:brand>/<string:user>/
This is an 'user' action, so the response event will be of type 'user'.
The event will contain a code if the user has earned the right to get one. Otherwise the respons is a standard error event.

2. POST https://url/discount-code/<string:brand>/
This is an 'administrative' action, so the response event will be of type 'administrative'.
This request will create 'count' number of discount-codes for the selected brand if the user has the right to execute this operation. Otherwise the respons is a standard error event.
The post fields are, 'prefix' and 'count'.
Example payload: {"prefix": "spring", "count": "100"}


## Standard error event
A standard error event can be of type 'user' or 'administrative'.
Then it will also contains the fields: 'errorcode' and 'message'
In a near future, a displaystring can be retrieved from the errorservice with this input.



