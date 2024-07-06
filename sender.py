from datetime import time

import pika

credential = pika.PlainCredentials('setare', 'setare')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', credentials=credential))
chanel = connection.channel()

chanel.exchange_declare(exchange='topic_logs', exchange_type='topic')
message = {
    'error.warning.important': 'this is important messages',
    'info.success.notImportant': 'this is not important messages',
}
for key, value in message.items():
    chanel.basic_publish(exchange='topic_logs', routing_key=key, body=value)

print('message Sent!')
connection.close()
