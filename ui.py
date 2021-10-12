from nameko.events import event_handler
from json import loads

def _show(type, payload):
    event = loads(payload)
    print(f'{type}-event: {event}')


class ConsoleUI:
    name = "ui"
    print('ui started')

    @event_handler('event_publisher', 'administrative')
    def handle_admin_event(self, payload):
        _show('admin', payload)

    @event_handler('event_publisher', 'user')
    def handle_user_event(self, payload):
        _show('user', payload)
