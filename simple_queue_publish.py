# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:44:11 2019

@author: schuhles
"""

import os
import pika

def simple_queue_publish(concurrency):
    amqp_url='amqp://oyuxrrne:gfgMfJSFtXMWivHwAfRzsKEp-ZAL0dMS@dove.rmq.cloudamqp.com/oyuxrrne'
    
    url = os.environ.get('CLOUDAMQP_URL',amqp_url)
    params = pika.URLParameters(url)
    params.socket_timeout = 5
    
    i = 0
    
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='presentation')
            
    if concurrency:
        while i < 1000:
               
            channel.basic_publish(exchange='',
                                  routing_key='presentation',
                                  body='Sixtine Schuhler-Husson',
                                  properties=pika.BasicProperties(
                                          delivery_mode = 2,))                      
            print(" [x] Sent 'Sixtine Schuhler-Husson'")
            i += 1
        
    else:
    
        channel.basic_publish(exchange='',
                              routing_key='presentation',
                              body='Sixtine Schuhler-Husson')
        print(" [x] Sent 'Sixtine Schuhler-Husson'")
    
    connection.close()