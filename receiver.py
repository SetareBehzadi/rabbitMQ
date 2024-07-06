import time

import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch = connection.channel()
ch.queue_declare('one')


def callback(ch, method, properties, body):
    print(f'Received message {body}')
    print(method)
    time.sleep(5)
    print( properties.type)
    print('done')
    ch.basic_ack(delivery_tag=method.delivery_tag)


ch.basic_qos(prefetch_count=1)
ch.basic_consume(queue='one', on_message_callback=callback)
print("Waiting for message, to exit press ctrl+c")
ch.start_consuming()
