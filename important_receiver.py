import pika

credentials = pika.PlainCredentials('setare','setare')
conn = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', credentials=credentials))
channel = conn.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
res = channel.queue_declare(queue='', exclusive=True)
channel.queue_bind(exchange='topic_logs', queue=res.method.queue, routing_key='#.important')

def callback(ch, method, properties, body):
    with open('error_files.log', 'a') as el:
        el.write(f'{str(body)} \n')


channel.basic_consume(queue=res.method.queue, auto_ack=True, on_message_callback=callback)
channel.start_consuming()


