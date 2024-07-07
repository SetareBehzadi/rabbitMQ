from datetime import time

import pika
from pika.exchange_type import ExchangeType

credential = pika.PlainCredentials('setare', 'setare')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credential))
chanel = connection.channel()

chanel.exchange_declare(exchange='headers_ex', exchange_type=ExchangeType.headers)
message = "hello world"
chanel.basic_publish(exchange='headers_ex', routing_key='', body=message, properties=pika.BasicProperties(headers={
                                                                                            'name':'rebbitmqTutorial', 'age':12}))
print('Sent....')
chanel.close()
