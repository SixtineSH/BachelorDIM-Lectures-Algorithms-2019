# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:55:23 2019

@author: schuhles
"""

import os
import pika

amqp_url='amqp://oyuxrrne:gfgMfJSFtXMWivHwAfRzsKEp-ZAL0dMS@dove.rmq.cloudamqp.com/oyuxrrne'

url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='prez') #name presentation didn't work

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(queue='prez',
     on_message_callback=callback,                          
     auto_ack=True)
    
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()