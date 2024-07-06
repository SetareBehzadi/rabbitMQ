import pika

credentials = pika.PlainCredentials('setare','setare')
conn= pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', credentials=credentials))
ch = conn.channel()

ch.exchange_declare(exchange='topic_logs', exchange_type='topic')
result = ch.queue_declare(queue='', exclusive=True)
ch.queue_bind(exchange='topic_logs', queue=result.method.queue, routing_key='*.*.notImportant')
print('Waiting for messages')


def callback(ch, method, properties, body):
    print(f'body : {body}')


ch.basic_consume(queue=result.method.queue, auto_ack=True, on_message_callback=callback)
ch.start_consuming()