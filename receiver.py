import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch = connection.channel()
ch.queue_declare('one')


def callback(ch, method, properties, body):
    print(f'Received message {body}')


ch.basic_consume(queue='one', on_message_callback=callback, auto_ack=True)
print("Waiting for message, to exit press ctrl+c")
ch.start_consuming()
