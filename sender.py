import pika

credential = pika.PlainCredentials('setare', 'setare')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credential))
chanel = connection.channel()

chanel.queue_declare('one')
chanel.basic_publish('', 'one','Bye rabbit')
print('message sent')
chanel.close()
