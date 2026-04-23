import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("projeto_nutricao_dados.xlsx")

df['IMC'] = df['Peso_kg'] / (df['Altura_m'] ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return 'Baixo Peso'
    elif 18.5 <= imc < 24.9:
        return 'Peso Normal'
    elif 25.0 <= imc < 29.9:
        return 'Sobrepeso'
    else:
        return 'Obesidade'

df['Status_Nutricional'] = df['IMC'].apply(classificar_imc)

print("Cálculos realizados com sucesso! Resumo da amostra:")
resumo = df['Status_Nutricional'].value_counts()
print(resumo)

sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 5))

grafico = sns.countplot(
    data=df,
    x='Status_Nutricional',
    hue='Status_Nutricional',
    palette='viridis',
    order=['Baixo Peso', 'Peso Normal', 'Sobrepeso', 'Obesidade']
)

plt.title('Distribuição do Status Nutricional (Amostra)', fontsize=14)
plt.xlabel('Categoria (OMS)', fontsize=12)
plt.ylabel('Número de Pacientes', fontsize=12)

plt.tight_layout()
plt.savefig('grafico_imc.png', dpi=300)
print("\nGráfico salvo com sucesso como 'grafico_imc.png'!")

plt.show()
