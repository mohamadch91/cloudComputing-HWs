AMQP_URL ="amqps://ncjjaxks:jLMl2Au8Mf3gQpntHV8IyfMGx7_HwBDt@turkey.rmq.cloudamqp.com/ncjjaxks"

import pika

def send_message(message):
    connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
    channel = connection.channel()

    channel.queue_declare(queue='Addqueue', durable=True)
    channel.basic_publish(exchange='', routing_key='Addqueue', body=message)
    print(" [x] Sent 'Hello World!'")
    connection.close()

def receive_message():
    connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
    channel = connection.channel()

    channel.queue_declare(queue='Addqueue', durable=True)
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue='Addqueue', on_message_callback=callback)
    channel.start_consuming()