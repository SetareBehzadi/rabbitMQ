import pika

credential = pika.PlainCredentials('setare','setare')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', credentials=credential))
ch = connection.channel()
ch.exchange_declare(exchange='logs', exchange_type='fanout')
ch.basic_publish(exchange='logs', routing_key='', body='fanout body...')
print('Message Sent')
connection.close()