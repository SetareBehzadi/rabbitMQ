import pika

credentials = pika.PlainCredentials('setare','setare')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1',credentials=credentials))
ch = connection.channel()

ch.exchange_declare('publisherConfirm', exchange_type='direct', auto_delete=False, durable=True)
ch.queue_declare('mainqqw', exclusive=False, auto_delete=False, durable=True)

ch.queue_bind('mainqqw','publisherConfirm', 'home')

def callback(ch, method, properties, body):
    print(f'get Request: {body}')


ch.basic_consume(queue='mainqqw', on_message_callback=callback)
print('start consume')
ch.start_consuming()