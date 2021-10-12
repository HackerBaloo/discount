from nameko.web.handlers import http
from nameko.rpc import RpcProxy, rpc
from random import randrange
from json import dumps, loads


class Discount:
    name = 'discount'

    #storage = RpcProxy('storage') #todo move this from endpoint to buissness logic class
    event = RpcProxy('event_publisher')


    @http('GET', '/discount/test/')
    def get_discount_test(self, request):
        print('test-endpoint')
        self.event.send_user_event('discount-test', 'event')
        return "handled"


    @http('GET', '/discount-code/<string:brand>/<string:user>/')
    def get_discount_code(self, request, brand, user):
        print('user-get')
        event = {}
        event['brand'] = brand
        event['user'] = user
        # todo get code from dependency injected impl
        code = 'spring2022'
        event['code'] = code
        self.event.send_user_event('discount-code-get', event)
        return "handled"

    @http('POST', '/discount-code/<string:brand>/')
    def create_discount_codes(self, request, brand):
        print('user-create')
        form_data = loads(request.get_data(as_text=True))
        prefix = form_data['prefix']
        count = form_data['count']
        data = {}
        code = f'{prefix}{randrange(0,10000)}'
        data['code'] = code
        data['count'] = count
        # todo move this from endpoint to buissness logic class
        json_data = dumps(data)
        #self.storage.store(brand, json_data)
        print(f'stored: {json_data} at: {brand}')
        event = {}
        event['count'] = count
        event['prefix'] = prefix
        self.event.send_admin_event('discount-code-post', event)

        return "handled"

