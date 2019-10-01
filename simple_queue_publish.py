# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:44:11 2019

@author: schuhles
"""

import os
import pika
import argparse

amqp_url='amqp://oyuxrrne:gfgMfJSFtXMWivHwAfRzsKEp-ZAL0dMS@dove.rmq.cloudamqp.com/oyuxrrne'

url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5


parser = argparse.ArgumentParser()
parser.add_argument("--concurrency", help="send to multiple queues",
                    action="store_true")
args = parser.parse_args()
i = 0

if args.concurrency==True:
    while i < 1000:
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        channel.queue_declare(queue='presentation')

        channel.basic_publish(exchange='',
                              routing_key='presentation',
                              body='Sixtine Schuhler-Husson',
                              properties=pika.BasicProperties(
                                      delivery_mode = 2))                      
        print(" [x] Sent 'Sixtine Schuhler-Husson'")
        connection.close()
        i += 1
    
else:
    #Send messages to the queue
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='presentation')

    channel.basic_publish(exchange='',
                          routing_key='presentation',
                          body='Sixtine Schuhler-Husson')
    print(" [x] Sent 'Sixtine Schuhler-Husson'")
    connection.close()