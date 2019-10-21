# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 09:33:03 2019

@author: schuhles
"""

import argparse
import simple_queue_publish as publish
import simple_queue_read as read

parser = argparse.ArgumentParser()
parser.add_argument("--read", help="read the script",
                    action="store_true")

parser.add_argument("--publish", help="publish the script",
                    action="store_true")

parser.add_argument("--concurrency", help="send to multiple queues",
                    action="store_true")
args = parser.parse_args()


if args.read:
    read.simple_queue_read(args.concurrency)

    
elif args.publish:
    publish.simple_queue_publish(args.concurrency)