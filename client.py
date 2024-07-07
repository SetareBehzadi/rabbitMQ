import pika

credential = pika.PlainCredentials('setare', 'setare')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credential))
ch = connection.channel()

ch.exchange_declare(exchange='first', exchange_type='direct')
ch.exchange_declare(exchange='second', exchange_type='fanout')

ch.exchange_bind('second', 'first')

ch.basic_publish(exchange='first', routing_key='', body='Hello world')

print('client Sent....')
connection.close()