# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:58:36 2019

@author: schuhles
"""

#import urlparse
import os
import pika
import config


mode='SEND' #set 'SEND' mode is you will to send rather than receive messages


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)



amqp_url=config.amqp_url

'amqp://oyuxrrne:gfgMfJSFtXMWivHwAfRzsKEp-ZAL0dMS@dove.rmq.cloudamqp.com/oyuxrrne'


# Parse CLODUAMQP_URL (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params) # Connect to CloudAMQP

channel = connection.channel()

channel.queue_declare(queue='hello')


if mode == 'SEND':
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!')
                          
    print(" [x] Sent 'Hello World!'")
    
    connection.close()
else:
        
    channel.basic_consume(queue='hello',
                          on_message_callback=callback,                          
                          auto_ack=True)
    
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()