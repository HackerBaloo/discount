from nameko.web.handlers import http
from nameko.rpc import RpcProxy


class GatewayService:
    name = 'gateway'

    queue = RpcProxy('queue_service')
    storage = RpcProxy('storage_service')

    @http('GET', '/discount-code/<string:brand>/<string:user>/')
    def get_discount_code(self, request, brand):
        airport = self.airports_rpc.get(airport_id)
        return 200

    @http('POST', '/discount-code/<string:brand>/')
    def post_airport(self, request):
        data = json.loads(request.get_data(as_text=True))
        airport_id = self.airports_rpc.create(data['airport'])

        return 200

    @http('GET', '/trip/<string:trip_id>')
    def get_trip(self, request, trip_id):
        trip = self.trips_rpc.get(trip_id)
        return 200

    @http('POST', '/trip')
    def post_trip(self, request):
        data = json.loads(request.get_data(as_text=True))
        trip_id = self.trips_rpc.create(data['airport_from'], data['airport_to'])

        return 200
