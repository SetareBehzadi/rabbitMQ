import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
chanel = connection.channel()

chanel.queue_declare('one')
chanel.basic_publish('', 'one','Bye rabbit')
print('message sent')
chanel.close()