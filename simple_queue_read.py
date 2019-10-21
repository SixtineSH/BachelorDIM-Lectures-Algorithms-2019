# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:55:23 2019

@author: schuhles
"""

import os
import pika

def simple_queue_read(concurrency):
    amqp_url='amqp://oyuxrrne:gfgMfJSFtXMWivHwAfRzsKEp-ZAL0dMS@dove.rmq.cloudamqp.com/oyuxrrne'
    url = os.environ.get('CLOUDAMQP_URL',amqp_url)
    params = pika.URLParameters(url)
    params.socket_timeout = 5
    
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='presentation')
    
    if concurrency:
    
        def callback(ch, method, properties, body):
            print(" [x] Received %r" % body)
            print(" [x] Message Processed, acknowledging (to delete message from the queue)")
            ch.basic_ack(delivery_tag = method.delivery_tag)
    
        channel.basic_consume(queue='presentation',
                              on_message_callback=callback,                          
                              auto_ack=True)
        channel.basic_qos(prefetch_count=1)
        
        channel.start_consuming()
    
    else:    
        def callback(ch, method, properties, body):
            print(" [x] Received %r" % body)
    
        channel.basic_consume(queue='presentation',
                              on_message_callback=callback,                    
                              auto_ack=True)
        
        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()