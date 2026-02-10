import producer_interface
import pika
import os

class mqProducer(producer_interface.mqProducerInterface):
    def __init__(self, routing_key: str, exchange_name: str) -> None:
        self.routing_key = routing_key
        self.exchange_name = exchange_name
        self.setupRMQConnection()

    def setupRMQConnection(self) -> None:
        # Build our connection to the RMQ Connection
        # params = pika.URLParameters('http://localhost:15672')
        # pika.PlainCredentials('guest', 'guest')
        conParams = pika.URLParameters(os.environ['AMQP_URL'])

        self.connection = pika.BlockingConnection(parameters=conParams)
        self.channel = self.connection.channel()

    def publishOrder(self, message: str) -> None:
        # Basic Publish to Exchange
        self.channel.basic_publish(
            exchange=self.exchange_name,
            routing_key=self.routing_key,
            body=message)

        # Close Channel
        self.channel.close()
        # Close Connection
        self.connection.close()
        pass
