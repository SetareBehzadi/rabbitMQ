import pika

credentials = pika.PlainCredentials('setare','setare')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1',credentials=credentials))
ch = connection.channel()

ch.exchange_declare(exchange='alt', exchange_type='fanout')
ch.exchange_declare(exchange='main', exchange_type='direct', arguments={'alternate-exchange':'alt'})

ch.basic_publish(exchange='main', routing_key='homee', body='Hello World')
print('Sent...!')
connection.close()