import pika
from pika.exchange_type import ExchangeType


credential = pika.PlainCredentials('setare', 'setare')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', credentials=credential))
ch = connection.channel()

ch.exchange_declare('headers_ex', ExchangeType.headers)
ch.queue_declare('que_any')


def callback(ch, method, properties, body):
    print(f'{body} is received')


bind_args = {'x-match':'any', 'name':'rebbitmqTutorial', 'age':5}
ch.queue_bind('que_any', 'headers_ex', arguments=bind_args)
ch.basic_consume(queue='que_any', auto_ack=True,on_message_callback=callback)
print('Waiting...')
ch.start_consuming()

