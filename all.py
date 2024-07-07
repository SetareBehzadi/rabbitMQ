import pika
from pika.exchange_type import ExchangeType


credential = pika.PlainCredentials('setare', 'setare')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', credentials=credential))
ch = connection.channel()

ch.exchange_declare(exchange='headers_ex', exchange_type=ExchangeType.headers)
ch.queue_declare(queue='que_all')
bind_args = {'x-match':'all', 'name':'rebbitmqTutorial', 'age':3}


def callback(ch, method, properties, body):
    print(f'{body} is receive')
    print('Waiting for logs')
    print(properties)

ch.queue_bind(queue='que_all', exchange='headers_ex', arguments=bind_args)
ch.basic_consume(queue='que_all', on_message_callback=callback, auto_ack=True)
print('Waiting...')
ch.start_consuming()

