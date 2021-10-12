from nameko.rpc import rpc
from nameko.events import EventDispatcher
from json import dumps


class EventPublisher:
    name = 'event_publisher'

    dispatch = EventDispatcher()

    @rpc
    def send_admin_event(self, operation, payload):
        event = {}
        event['type'] = 'administrative'
        event['payload'] = payload
        self._send_event(operation, event)

    @rpc
    def send_user_event(self, operation, payload):
        event = {}
        event['type'] = 'user'
        event['payload'] = payload
        self._send_event(operation, event)

    def _send_event(self, operation, event):
        event['operation'] = operation
        type_info = event['type']
        print(f'sending event, type: {type_info}, operation: {operation}')
        json = dumps(event)
        self.dispatch(type_info, json)
        print('sent')


