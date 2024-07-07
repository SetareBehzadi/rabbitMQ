import pika

credential = pika.PlainCredentials('setare', 'setare')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credential))
ch = connection.channel()

ch.exchange_declare(exchange='second',exchange_type='fanout')
ch.queue_declare('Setare')
ch.queue_bind('Setare', 'second')

def callback(ch, method, properties, body):
    print(f'received {body}')

ch.basic_consume('Setare', on_message_callback=callback, auto_ack=True)
print('Start Consuming')
ch.start_consuming()