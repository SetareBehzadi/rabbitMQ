import pika

credentials = pika.PlainCredentials('setare','setare')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1',credentials=credentials))
ch = connection.channel()

ch.exchange_declare(exchange='alt', exchange_type='fanout')
ch.exchange_declare(exchange='main', exchange_type='direct', arguments={'alternate-exchange':'alt'})

ch.queue_declare(queue='altq')
ch.queue_bind('altq', 'alt')

ch.queue_declare(queue='mainq')
ch.queue_bind('mainq', 'main','home')


def main_callback(ch, method, properties, body):
    print(f'main call: {body}')


def alt_callback(ch, method, properties, body):
    print(f'alt call:{body}')


ch.basic_consume('mainq', on_message_callback=main_callback, auto_ack=True)
ch.basic_consume('altq', on_message_callback=alt_callback, auto_ack=True)

print('Start consuming.')
ch.start_consuming()