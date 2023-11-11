from channels.generic.websocket import WebsocketConsumer
from json import dumps, loads


class TestConsumer(WebsocketConsumer):
    def connect(self):
        print("Connection Recieved")
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        # text_data_json = loads(text_data)
        # message = text_data_json["message"]

        print(text_data)

        self.send(text_data=dumps({"message": "hello"}))
