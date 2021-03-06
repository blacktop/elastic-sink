__author__ = 'blacktop'

from kafka import KafkaConsumer
import dns.resolver

myResolver = dns.resolver.Resolver()
myResolver.nameservers = ['172.16.197.191']
myAnswers = myResolver.query("kafka.service.consul", "SRV")
IP = myAnswers.response.additional[0].items[0].address
PORT = myAnswers.response.answer[0].items[0].port

# To consume messages
consumer = KafkaConsumer('my-topic', group_id='my_group', bootstrap_servers=['{}:{}'.format(IP, PORT)])
# consumer = KafkaConsumer('my-topic', group_id='my_group', bootstrap_servers=['127.0.0.1:9092'])
for message in consumer:
    # message value is raw byte string -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))
