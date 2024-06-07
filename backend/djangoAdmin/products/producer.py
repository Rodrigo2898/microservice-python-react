import pika
import json

# Create connection with RabbitMQ
params = pika.URLParameters('amqps://lvdgbfat:GAwkmDDOhZsh0i2K0XX4QtmRcDuoAUp8@gull.rmq.cloudamqp.com/lvdgbfat')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)

