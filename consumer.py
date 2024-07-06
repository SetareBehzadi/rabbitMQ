import pika

credentials = pika.PlainCredentials('setare','setare')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1',credentials=credentials))
ch = connection.channel()
ch.exchange_declare(exchange='logs', exchange_type='fanout')
result = ch.queue_declare(queue='', exclusive=True) # saf enhesari hast va etesal ghat beshe inam hazv mishe

ch.queue_bind(exchange='logs', queue=result.method.queue)
print('Waiting for logs')
print(result)
print(f'ssss {result.method.queue}')


def callback(ch, method, properties, body):
    print(f'Recieve {body}')


ch.basic_consume(queue=result.method.queue, on_message_callback=callback)
ch.start_consuming()