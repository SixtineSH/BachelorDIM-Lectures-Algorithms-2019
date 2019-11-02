# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:44:11 2019

@author: schuhles
"""  

import os
import pika
import config
import getpass


def callback(ch, method, properties, body):
    ##
    #Function that prints the published message
    #Args:ch, method, properties, body
    #Returns nothing
    print(" [x] Received %r" % body)


def simple_queue_publish(concurrency, number = 1):
    ##
    #Function that sends a message
    #Args:concurrency, number
    #Returns nothing

    amqp_url=config.amqp_url

    # Parse CLODUAMQP_URL (fallback to localhost)
    url = os.environ.get('CLOUDAMQP_URL',amqp_url)
    params = pika.URLParameters(url)
    params.socket_timeout = 5

    connection = pika.BlockingConnection(params) # Connect to CloudAMQP

    properties = pika.BasicProperties()
    if concurrency:
        properties.delivery_mode = 2
        print('persitent mode')

    channel = connection.channel()
    channel.queue_declare(queue='presentation')

    for i in range(1, number+1):
        channel.basic_publish(exchange='',
                              routing_key='presentation',
                              body=getpass.getuser(),
                              properties = properties)                 
        print(" [{0}] Sent '{1}'".format(i,getpass.getuser()))

    connection.close()