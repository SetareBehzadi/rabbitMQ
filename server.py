import pika

credentials = pika.PlainCredentials('setare','setare')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1',credentials=credentials))
ch = connection.channel()

ch.exchange_declare('acceptReject', exchange_type='fanout')
ch.queue_declare(queue='nackq')

ch.queue_bind('nackq', 'acceptReject')

def callback(ch, method, properties, body):
    if method.delivery_tag % 5 == 0:
        ch.basic_nack(delivery_tag=method.delivery_tag, multiple=True, requeue=False)
    print(f'get Request: {method.delivery_tag}')


ch.basic_consume(queue='nackq', on_message_callback=callback)
print('start consume')
ch.start_consuming()