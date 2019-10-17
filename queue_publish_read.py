# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 09:33:03 2019

@author: schuhles
"""

import pika
import os
import argparse

amqp_url='amqp://oyuxrrne:gfgMfJSFtXMWivHwAfRzsKEp-ZAL0dMS@dove.rmq.cloudamqp.com/oyuxrrne'
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

parser = argparse.ArgumentParser()
parser.add_argument("--read", help="read the script",
                    action="store_true")
args = parser.parse_args()

cpt = 0 #to know th numbers of received messages

if args.read==True:
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='presentation')
    cpt = 0

    def callback(ch, method, properties, body):
            ##
            #Function that receive and print messages from the queue
            #Returns : The received messages and the count
        print(" [x] Received %r" % body)
        global cpt
        cpt += 1
        print('Count = %d' %cpt)        

    channel.basic_consume(queue='presentation',
                          on_message_callback=callback,                          
                          auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    
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