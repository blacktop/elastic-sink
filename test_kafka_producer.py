# -*- coding: utf-8 -*-
__author__ = 'blacktop'

import json
from kafka import SimpleProducer, KafkaClient
import dns.resolver

myResolver = dns.resolver.Resolver()
myResolver.nameservers = ['172.16.197.191']
myAnswers = myResolver.query("kafka.service.consul", "SRV")
IP = myAnswers.response.additional[0].items[0].address
PORT = myAnswers.response.answer[0].items[0].port
print 'Using Kafka Host: {}:{}'.format(IP, PORT)

# To send messages synchronously
kafka = KafkaClient('{}:{}'.format(IP, PORT))
# kafka = KafkaClient('127.0.0.1:9092')
producer = SimpleProducer(kafka)

tet = dict(this='EEEEEEEEHHHHH!', _is=['one', 'two', 'buckle my shoe, bitch!'], awesome=dict(look_mom='no hands'))

# Note that the application is responsible for encoding messages to type bytes
producer.send_messages(b'my-topic', b'some message')
producer.send_messages(b'my-topic', b'this method', b'is variadic')
producer.send_messages(b'my-topic', json.dumps(tet))

# Send unicode message
producer.send_messages(b'my-topic', u'你怎么样?'.encode('utf-8'))
