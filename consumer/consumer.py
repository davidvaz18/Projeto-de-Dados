from kafka import KafkaConsumer
import json
import multiprocessing


evento_de_parada = multiprocessing.Event()  

def main():
    consumer = KafkaConsumer(bootstrap_servers = 'localhost:9092')
    consumer.subscribe(['coba'])
    while not evento_de_parada.is_set():
        for message in consumer:
            print(" Topic: " + str(message[0])
            + "\n Message: " + str(message[6], 'utf-8')
            + "\n Record: " + str(message))
            if evento_de_parada.is_set():
                break

    consumer.close()

if __name__ == '__main__':
    main()