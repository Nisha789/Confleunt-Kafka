from confluent_kafka import DeserializingConsumer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroDeserializer
from confluent_kafka.serialization import StringDeserializer

# Define Kafka Configuration
kafka_config = {
    'bootstrap.servers': 'host:9092',
    'sasl.mechanisms': 'PLAIN',
    'security.protocol': 'SASL_SSL',
    'sasl.username': 'ABC',
    'sasl.password': 'XYZ',
    'group.id': 'group1',
    'auto.offset.reset': 'earliest'
}

# Create a Schema Registry Client
schema_registry_client = SchemaRegistryClient({
    'url':'url1',
    'basic.auth.user.info':'{}:{}'.format('abc','xyz')
})

# Fetch the latest avro schema for the value
subject_name = 'retail_data_test-value'
schema_str = schema_registry_client.get_latest_version(subject_name).schema.schema_str

# Create Avro Deserializer for the value
key_deserializer = StringDeserializer('utf-8')
avro_deserializer = AvroDeserializer(schema_registry_client,schema_str)

# Define the Deserializing Consumer
consumer = DeserializingConsumer({
    'bootstrap.servers': kafka_config['bootstrap.servers'],
    'security.protocol': kafka_config['security.protocol'],
    'sasl.mechanisms': kafka_config['sasl.mechanisms'],
    'sasl.username': kafka_config['sasl.username'],
    'sasl.password': kafka_config['sasl.password'],
    'group.id': kafka_config['group.id'],
    'auto.offset.reset': kafka_config['auto.offset.reset']
})

# Subscribe to the 'retail_data_test' topic
consumer.subscribe(['retail_data_test'])

# Continually read messages from kafka
try:
    while True: # Because consumer needs to listen messages continuosuly
        msg = consumer.poll(1.0) # How many seconds to wait for message
        
        if msg is None:
            continue
        if msg.error():
            print('COnsumer error: {}'.format(msg.error()))
            continue
        
        print('Successfully consumed record with key {} and value {}'.format(msg.key(),msg.value()))
        
except KeyboardInterrupt:
    pass
finally:
    consumer.close()