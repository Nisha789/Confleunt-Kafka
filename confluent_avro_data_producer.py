import pandas as pd
import time
from time import sleep

from confluent_kafka import SerializingProducer

from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer
from confluent_kafka.serialization import StringSerializer

# Define Kafka Configuration
kafka_config = {
    'bootstrap.servers': 'pkc-7prvp.centralindia.azure.confluent.cloud:9092',
    'sasl.mechanisms': 'PLAIN', # for secured authentication
    'security.protocol': 'SASL_SSL', # for secured authentication
    'sasl.username': 'VG7C52XOFINQF3MK', # Cluster API Key
    'sasl.password': 'GRiq/Y8ImvA5KOs2olcFm7E5u0hOausYjiGpE68SrxvMvgQmi2JLoYg/g4YY9bQw' # Cluster API Password
} 

# Create a Schema Registry Client
schema_registry_client = SchemaRegistryClient({
    'url':'https://psrc-7yxz9w.southeastasia.azure.confluent.cloud',
    'basic.auth.user.info':'{}:{}'.format('H3JREM4NAKCCYWW3','6ePl6mjPJ9+a+TZ1hcs6pPzC7hNq5G/g3e2HNjcnRNecP/7vhML95k3MDyC8O4Ov') # Schema API Key and Password not cluster one
})

# Fetch the latest Avro Schema for the value
subject_name = 'retail_data_test-value'
schema_str = schema_registry_client.get_latest_version(subject_name).schema.schema_str

# Create Avro Serializer for the value
key_serializer = StringSerializer('utf-8')
avro_serializer = AvroSerializer(schema_registry_client,schema_str)

# Define the Serializing Producer
producer = SerializingProducer({
    'bootstrap.servers': kafka_config['bootstrap.servers'],
    'security.protocol': kafka_config['security.protocol'],
    'sasl.mechanisms': kafka_config['sasl.mechanisms'],
    'sasl.username': kafka_config['sasl.username'],
    'sasl.password': kafka_config['sasl.password'],
    'key.serializer': key_serializer, # Key will be serialized as a string
    'value.serializer': avro_serializer # Value will be serialized as Avro
})

def delivery_report(err, msg): # For logging purpose
    if err is not None:
        print("Delivery failed for User record {}: {}".format(msg.key(), err))
        return
    print('User record {} successfully produced to {} [{}] at offset {}'.format(
        msg.key(), msg.topic(), msg.partition(), msg.offset()))

# Load the CSV data into a pandas dataframe
df = pd.read_csv("retail_data.csv")
df = df.fillna("null")
# print(df.head())

# Iterate over DataFrame rows and produce to Kafka
for index,row in df.iterrows():
    
    # Create a dictionary from the row values
    value = row.to_dict()
    # print(value)
    
    # Produce to Kafka
    producer.produce(topic='retail_data_test',key=str(index),value=value,on_delivery=delivery_report)
    producer.flush()
    time.sleep(2) # 2 seconds
    
print("All Data successfully published to Kafka")