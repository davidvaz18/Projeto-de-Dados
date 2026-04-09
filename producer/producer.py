import json
import time
import random
from datetime import datetime
import uuid
import logging

#Lista simplificada para o simulador
medicamentos = [
    {"nome" : "Amoxicilina", "categoria": "Antibiotico", "preco": 45.50},  
    {"nome": "Dipirona", "categoria": "Analgésico", "preco": 12.00},
    {"nome": "Paracetamol", "categoria": "Analgésico", "preco": 15.00},
    {"nome": "Insulina", "categoria": "Diabetes", "preco": 89.90}
]

def gerar_eventos_estoque():
    med = random.choice(medicamentos)
    qtd = random.randint(1,5)* (-1 if random.random()< 0.8 else 1)

    evento = {
        "id_transacao" : str(uuid.uuid4()),
        "medicamento" : med["nome"],
        "timestamp" : datetime.now().isoformat(),
        "preco_unitario": med["preco"],
        "categoria": med["categoria"],
        "quantidade" : qtd
    }
    return evento

if __name__ == "__main__":
    print("Iniciando Simulador de Farmácia...")
    try:
            while True:
                 dado = gerar_eventos_estoque()
                 print(f"[LOG]{dado['timestamp']} - {dado['medicamento']}: {dado['quantidade']} unidades")


                 time.sleep(random.uniform(0.5,3.0)) # simulando tempo real variavel

                 
    except KeyboardInterrupt:
         print("\n Simulação Interrompida")