import time

import pika

credentials = pika.PlainCredentials('setare', 'setare')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', credentials=credentials))
ch = connection.channel()
ch.exchange_declare('publisherConfirm', exchange_type='direct', auto_delete=False, durable=True)
ch.queue_declare('mainqqw', exclusive=False, auto_delete=False, durable=True)

ch.queue_bind('mainqqw', 'publisherConfirm', 'home')
ch.confirm_delivery()

for i in range(20):
    try:
        ch.basic_publish('publisherConfirm', 'home', body='Hello', properties=pika.BasicProperties(
            content_type='text/plain',
            delivery_mode=2),
                         mandatory=True)
        print(f'message: {i}')
    except Exception as e:
        print(f'Exception:{type(e).__name__}')
    time.sleep(2)

while True:
    ch.basic_publish(exchange='acceptReject', routing_key='home', body='Hello world...')
    print('sent...')
    input('Press any key to continue...')
