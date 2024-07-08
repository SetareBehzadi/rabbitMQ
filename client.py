import pika

credentials = pika.PlainCredentials('setare','setare')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1',credentials=credentials))
ch = connection.channel()

ch.exchange_declare(exchange='mains', exchange_type='direct')

ch.basic_publish(exchange='mains', routing_key='home', body='Hello World')
print('Sent...!')
connection.close()