# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 09:33:03 2019

@author: schuhles
"""

import argparse
import simple_queue_publish as publish
import simple_queue_read as read

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--read', help="read the script",
                    action="store_true")

parser.add_argument('-p', '--publish', help="publish the script",
                    action="store_true")

parser.add_argument('-c', '--concurrency', help="send to multiple queues",
                    action="store_true")
parser.add_argument('-s', '--slow', help="slow reader",
                    action='store_true')
args = parser.parse_args()


if args.read:
    read.simple_queue_read(args.concurrency, args.slow)

elif args.publish:
    publish.simple_queue_publish(args.concurrency)

else:
    print('Please specify --read or --publish')