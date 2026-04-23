import pandas as pd
import random
from faker import Faker

fake = Faker('pt_BR') 

num_pacientes = 50
dados = []

# Listas para simular dados qualitativos
sintomas_clinicos = [
    "Sem alterações visíveis", "Palidez na conjuntiva", "Cabelo quebradiço",
    "Manchas de Bitot", "Sangramento gengival", "Pele seca", "Edema leve"
]

refeicoes_exemplo = [
    "Café com leite e pão com manteiga", "Arroz, feijão e bife",
    "Lasanha congelada e refrigerante", "Salada de frutas e iogurte",
    "Sanduíche de presunto e queijo", "Feijoada completa e laranja"
]

for _ in range(num_pacientes):
    peso = round(random.uniform(50.0, 120.0), 1)
    altura = round(random.uniform(1.50, 1.95), 2)
    cintura = random.randint(60, 110)
    quadril = random.randint(80, 130)

    dieta_desc = f"Manhã: {random.choice(refeicoes_exemplo)}. Almoço: {random.choice(refeicoes_exemplo)}."
    sinal_clinico = random.choice(sintomas_clinicos)

    dados.append({
        "ID_Paciente": fake.uuid4()[:8],
        "Nome": fake.name(),
        "Idade": random.randint(18, 65),
        "Peso_kg": peso,
        "Altura_m": altura,
        "Cintura_cm": cintura,
        "Quadril_cm": quadril,
        "Recordatorio_24h": dieta_desc,  # Texto para sua IA processar depois
        "Sinais_Clinicos": sinal_clinico
    })

df = pd.DataFrame(dados)
df.to_excel("projeto_nutricao_dados.xlsx", index=False)

print("Arquivo 'projeto_nutricao_dados.xlsx' gerado com sucesso!")
