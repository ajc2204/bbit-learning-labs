from consumer_interface import mqConsumerInterface
import pika
import os

class mqConsumer(mqConsumerInterface):
    def __init__(self, binding_key: str, exchange_name: str, queue_name: str) -> None:
         # Save parameters to class variables
        self.binding_key = binding_key
        self.exchange_name = exchange_name
        self.queue_name = queue_name

        # Call setupRMQConnection
        self.setupRMQConnection()
        pass

    def setupRMQConnection(self):
        #Build our connection to the RMQ Connection.
        #The AMPQ_URL is a string which tells pika the package the URL of our AMPQ service in this scenario RabbitMQ.
        conParams = pika.URLParameters(os.environ['AMQP_URL'])
        connection = pika.BlockingConnection(parameters=conParams)
        self.channel = connection.channel()
        self.channel.exchange_declare('Tech Lab Exchange')

        self.channel.queue_declare(queue=self.queue_name)
        self.channel.queue_bind(queue= self.queue_name, routing_key= self.binding_key, exchange=self.exchange_name)
        self.channel.basic_consume(self.queue_name, self.body.message)

    def onMessageCallback(self):
        self.channel.basic_ack(method_frame.delivery_tag, False)

    def startConsuming(self):
        print(" [*] Waiting for messages. To exit press CTRL+C")
        self.channel.start_consuming()

    def __del__(self):
        self.channel.close()
        print("Closing RMQ connection on destruction")
        self.connection.close()
    