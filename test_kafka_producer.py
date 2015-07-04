# -*- coding: utf-8 -*-
__author__ = 'blacktop'

import json
from kafka import SimpleProducer, KafkaClient

# To send messages synchronously
kafka = KafkaClient('172.16.197.191:9092')
producer = SimpleProducer(kafka)

tet = dict(this='EEEEEEEEHHHHH!', _is=['one', 'two', 'buckle my shoe, bitch!'], awesome=dict(look_mom='no hands'))

# Note that the application is responsible for encoding messages to type bytes
producer.send_messages(b'my-topic', b'some message')
producer.send_messages(b'my-topic', b'this method', b'is variadic')
producer.send_messages(b'my-topic', json.dumps(tet))

# Send unicode message
producer.send_messages(b'my-topic', u'你怎么样?'.encode('utf-8'))
