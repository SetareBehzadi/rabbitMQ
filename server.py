import pika

credentials = pika.PlainCredentials('setare','setare')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1',credentials=credentials))
ch = connection.channel()

ch.exchange_declare(exchange='mains', exchange_type='direct')
ch.exchange_declare(exchange='delx', exchange_type='fanout')

ch.queue_declare(queue='mainqq', arguments={'x-dead-letter-exchange': 'delx', 'x-message-ttl': 5000, "x-max-length": 10})

ch.queue_bind('mainqq', 'mains', 'home')

ch.queue_declare(queue='delxq')
ch.queue_bind('delxq', 'delx')

def delx_callback(ch, method, properties, body):
    print(f'delx call: {body}')

#
# ch.basic_consume('mainq', on_message_callback=main_callback, auto_ack=True)
ch.basic_consume('delxq', on_message_callback=delx_callback, auto_ack=True)

print('Start consuming.')
ch.start_consuming()