import pika

credentials = pika.PlainCredentials('setare','setare')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1',credentials=credentials))
ch = connection.channel()
ch.exchange_declare('acceptReject', exchange_type='fanout')

while True:
    ch.basic_publish(exchange='acceptReject',routing_key='home', body='Hello world...')
    print('sent...')
    input('Press any key to continue...')
