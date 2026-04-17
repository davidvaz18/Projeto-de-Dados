from kafka import KafkaConsumer
import json
import multiprocessing


evento_de_parada = multiprocessing.Event()  

def main():
    consumer = KafkaConsumer(
    'coba',
    bootstrap_servers = 'localhost:9092',
    auto_offset_reset = 'latest',
    value_deserializer= lambda x: json.loads(x.decode('utf-8'))    
    )

    print("Consumer esperando atualizações da farmácia...")

    try:
        while not evento_de_parada.is_set():
            for message in consumer:
                dado = message.value
                print(f"   [RECEBIDO] Tópico: {message.topic}")
                print(f"   Medicamento: {dado['medicamento']}")
                print(f"   Quantidade: {dado['quantidade']}")
                print(f"   Horário: {dado['timestamp']}")
                print("-" * 40)
                if evento_de_parada.is_set():
                    break
    except KeyboardInterrupt:
        print("Ação interrompida")
    finally:
        consumer.close()

if __name__ == '__main__':
    main()