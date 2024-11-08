# Confluent Kafka Producer and Consumer Example

This repository contains an example project demonstrating how to produce and consume Avro data using Confluent Kafka. The project includes Python scripts to interact with Kafka and manage data in Avro format.

## Project Files

- `confluent_avro_data_consumer.py`: The Python script used to consume Avro data from Kafka.
- `confluent_avro_data_producer.py`: The Python script used to produce Avro data to Kafka.
- `retail_data.csv`: Sample data file in CSV format used to produce Avro messages.
- `retail_data_avro_schema.json`: The Avro schema used to serialize the `retail_data.csv` file to Avro format.

## Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.x
- Confluent Kafka in a cloud environment
- Required Python libraries:
  - `confluent_kafka`
  - `json`

You can install the required Python libraries by running the following command:


## Setup

1. **Kafka Setup**: Ensure access to a Kafka instance.

2. **Avro Schema**: The `retail_data_avro_schema.json` file contains the Avro schema used for data serialization. Make sure it matches the structure of your data (in this case, `retail_data.csv`).

3. **Modify Kafka Configurations**: Update the Kafka configurations in both the producer and consumer scripts (`confluent_avro_data_producer.py` and `confluent_avro_data_consumer.py`) to match your Kafka instance details, including the topic and broker information.

## Usage

### Producing Data to Kafka

To start producing data to Kafka, run the following script: `confluent_avro_data_producer.py`

This will read the `retail_data.csv`, serialize it using the Avro schema (`retail_data_avro_schema.json`), and produce the messages to the specified Kafka topic.

### Consuming Data from Kafka

To consume data from Kafka, run the following script: `confluent_avro_data_consumer.py`

This script will consume Avro messages from the Kafka topic and print the deserialized data.

## Example Workflow

1. The producer script reads the CSV data from `retail_data.csv`.
2. The data is serialized to Avro format using the schema defined in `retail_data_avro_schema.json`.
3. The producer sends the Avro data to a Kafka topic.
4. The consumer script listens to the Kafka topic and consumes the Avro messages.
5. The consumer deserializes the Avro data and prints it.

## Contributions
Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request with your enhancements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Confluent Kafka**: This project uses Confluent Kafka for message brokering and data streaming. [Confluent Kafka](https://www.confluent.io/) provides a robust platform for handling real-time data streams.
- **Python Libraries**: The project leverages `confluent_kafka` Python library for integrating with Kafka.

