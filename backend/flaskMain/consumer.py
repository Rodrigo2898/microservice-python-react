import pika

# Create connection with RabbitMQ
params = pika.URLParameters('amqps://lvdgbfat:GAwkmDDOhZsh0i2K0XX4QtmRcDuoAUp8@gull.rmq.cloudamqp.com/lvdgbfat')

connection = pika.BlockingConnection(params)

channel = connection.channel()


channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Receive in main')
    print(body)


channel.basic_consume(queue='main', on_message_callback=callback)


print('Starting consumer')

channel.start_consuming()

channel.close()
