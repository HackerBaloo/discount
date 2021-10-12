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


## Setup

1. `python3 -m venv venv`
2. `. ./venv/bin/activate`
3. `pip install nameko`
4. `pip install nameko-redis` (storage service is not yet used)
5. `pip install nameko-mongodb` (not yet used)
6. docker run -p 5672:5672 --hostname nameko-rabbitmq

### For test
7. Start 4 terminal windows, arranged so you can look at them all
8. In all of them run : `. ./venv/bin/activate`
9. In #1 `nameko run ui`
10. In #2 `nameko run event_publisher`
11. In #3 `nameko run discount`
12. In #4 `curl -i localhost:8000/discount-code/coop/nils/`
13. In #4 `curl -i -d "{\"prefix\": \"blow\", \"count\": \"100\"}" localhost:8000/discount-code/coop`
After executing the requests you should reactions in all of the windows.


## Roadmap
0. Intervju the business owner to better understand the needs.
1. Finish the docker compose work to make setup and testing easier.
2. Start using the storage module, only MongoDB or in combination with Redis?






