import pika


credential = pika.PlainCredentials('setare', 'setare')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', credentials=credential))
ch=connection.channel()

ch.queue_declare(queue='queue_request')


def on_request_message_received(ch, method, properties, body):
    print(f'Received request: {properties.correlation_id}')
    ch.basic_publish('', routing_key=properties.reply_to, body=f'reply tp {properties.correlation_id}')


ch.basic_consume(queue='queue_request', auto_ack=True, on_message_callback=on_request_message_received)
print('Starting Server...!')
ch.start_consuming()

