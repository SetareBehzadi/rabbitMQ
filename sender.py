from datetime import time

import pika

credential = pika.PlainCredentials('setare', 'setare')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credential))
chanel = connection.channel()

chanel.queue_declare('one')
chanel.basic_publish('', 'one','Bye rabbit',
                     properties=pika.BasicProperties(
                        content_type='text/plain',
                         content_encoding='gzip',
                         timestamp=100000000,
                         delivery_mode=2,
                         user_id="setare",
                         type="exchange.queue",
                         headers={"name":'amir', 'age':30}
                     )
                     )
print('message sent')
chanel.close()
