import pika
import json

def produce_content(msg):
    try:
        # establish connection to RabbitMQ
        url = pika.URLParameters('amqps://dzpcyzjh:d29a-usR4GLTaivnyiYkk2tbpJIdOsnX@puffin.rmq2.cloudamqp.com/dzpcyzjh')
        connection = pika.BlockingConnection(url)
        channel = connection.channel()

        # declare exchange and queue
        channel.exchange_declare(exchange='exchange', exchange_type='direct', durable=True)
        channel.queue_declare(queue='review_py', durable=False)
        channel.queue_bind(exchange='exchange', queue='review', routing_key='routing_key')

        # publish message
        channel.basic_publish(
            exchange='exchange',
            routing_key='routing_key',
            body=json.dumps(msg),  
            properties=pika.BasicProperties(
                delivery_mode=2  
            )
        )
        print(f"Message sent: {msg}")

        connection.close()
    except Exception as e:
        print(f"An error occurred: {e}")
