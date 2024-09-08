
'''
// this part is set up for another back end
// it is not part this back end

'''
from dotenv import load_dotenv
import pika
import os

load_dotenv()
url = os.getenv('URL')

def callback(ch, method, properties, body):
    print("Message received:", body.decode())
    # If you set auto_ack=False, you need to acknowledge the message
    ch.basic_ack(delivery_tag=method.delivery_tag)

def consume_content():
    try:
        url = pika.URLParameters(url)
        connection = pika.BlockingConnection(url)
        channel = connection.channel()

        # Set up the exchange and queue
        print("Declaring queue...")
        channel.queue_declare(queue='review', durable=False)
        print("Binding queue to exchange...")
        channel.queue_bind(exchange='exchange', queue='review', routing_key='routing_key')

        # Set up the consumer
        print("Setting up consumer...")
        channel.basic_consume(queue='review', on_message_callback=callback, auto_ack=True)

        print('Waiting for messages...')
        channel.start_consuming()
    except pika.exceptions.AMQPError as e:
        print("Error connecting to RabbitMQ:", e)

