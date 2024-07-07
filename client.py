import pika
import uuid

credential = pika.PlainCredentials('setare', 'setare')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credential))
ch = connection.channel()
# saf eijad kardim baraye pasokh hayi ke migirim va chap mikonim
reply_queue = ch.queue_declare('', exclusive=True)


def on_reply_message_receive(ch, method, properties, body):
    print(f'reply received: {body}')


# pasokhi biad migire va namayesh mide
ch.basic_consume(queue=reply_queue.method.queue, auto_ack=True, on_message_callback=on_reply_message_receive)

# baraye gereftan pasokh darkhst hayi mifreste ke inja namayesh mide
ch.queue_declare(queue='queue_request')
core_id = str(uuid.uuid4())
print(f'Sending request {core_id}')

ch.basic_publish(exchange='', routing_key='queue_request', properties=pika.BasicProperties(
                                                                            reply_to=reply_queue.method.queue,
                                                                            correlation_id=core_id ),
                                                            body='Can I request a reply')

print('Start Client ...')
ch.start_consuming()
