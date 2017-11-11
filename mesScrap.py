from kafka import KafkaProducer, KafkaConsumer

class Producer():

    consumer = ''
    producer = ''

    def __init__(self):
        """
            Initialize the kafka Producer
        """
        self.producer = KafkaProducer(bootstrap_servers='localhost:9092'
                                 ,api_version=(0,10))

    def SendMsg(self, topic, msg):
        """
            Sending json to kafka topic
        """
        self.producer.send(topic, 'hola')#bytes(msg, 'utf-8'))
        print(msg)

class Consumer():

    def __init__(self):
        """
            Initialize kafka consumer
        """
        self.consumer = KafkaConsumer(bootstrap_servers='localhost:9092'
                                ,auto_offset_reset='earliest'
                                ,api_version=(0,10))

    def Read(self, topic):
        """
            Read kafka messages send by producer
        """
        self.consumer.subscribe([topic])
        for msg in self.consumer:
            print(msg)
