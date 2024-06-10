import pika, json
from products.models import Product

# Create connection with RabbitMQ
params = pika.URLParameters('amqps://lvdgbfat:GAwkmDDOhZsh0i2K0XX4QtmRcDuoAUp8@gull.rmq.cloudamqp.com/lvdgbfat')

connection = pika.BlockingConnection(params)

channel = connection.channel()


channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Receive in admin')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased!')


channel.basic_consume(queue='admin', on_message_callback=callback)


print('Starting consumer')

channel.start_consuming()

channel.close()
