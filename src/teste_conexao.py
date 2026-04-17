from kafka import KafkaProducer

print("⏳ Tentando conectar ao Kafka no Docker...")

try:
    producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')
    print("✅ SUCESSO! O Python conseguiu falar com o Kafka.")
    producer.close()
except Exception as e:
    print(f"❌ ERRO: Não conectou. Motivo: {e}") #w