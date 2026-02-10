from producer import producer_interface
import pika

class mqProducer(producer_interface.mqProducerInterface):
    def __init__(self, routing_key: str, exchange_name: str) -> None:
        self.routing_key = routing_key
        self.exchange_name = exchange_name
        self.connection 
        self.channel
        self.setupRMQConnection()

def setupRMQConnection(self) -> None:
    # Build our connection to the RMQ Connection
    self.connection = pika.BlockingConnection(pika.ConnectionParamters('localhost'))
    self.channel = self.connection.channel()

def publishOrder(self, message: str) -> None:
    # Basic Publish to Exchange
    self.channel.queue_declare(queue='queue')
    self.basic_publish(exchange=self.exchange_name,
                       routing_key=self.routing_key,
                       body=message)

    # Close Channel
    self.channel.close()
    # Close Connection
    self.connection.close()
    pass