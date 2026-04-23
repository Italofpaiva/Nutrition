import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Ler os dados (vamos usar o Excel original que tem o Peso e Altura)
df = pd.read_excel("projeto_nutricao_dados.xlsx")

# 2. Lógica de Negócio: Calcular o IMC (Peso / Altura²)
# O Pandas faz o cálculo para as 50 linhas de uma vez só!
df['IMC'] = df['Peso_kg'] / (df['Altura_m'] ** 2)

# 3. Lógica de Negócio: Classificar o IMC segundo a OMS (Valores de Referência)
def classificar_imc(imc):
    if imc < 18.5:
        return 'Baixo Peso'
    elif 18.5 <= imc < 24.9:
        return 'Peso Normal'
    elif 25.0 <= imc < 29.9:
        return 'Sobrepeso'
    else:
        return 'Obesidade'

# Aplica a regra para criar uma nova coluna de "Status"
df['Status_Nutricional'] = df['IMC'].apply(classificar_imc)

print("Cálculos realizados com sucesso! Resumo da amostra:")
# Mostra uma tabela de resumo de quantas pessoas estão em cada categoria
resumo = df['Status_Nutricional'].value_counts()
print(resumo)

# 4. Visualização de Dados (Gerando o Gráfico)
# Configurar o estilo visual do gráfico
sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 5))

# Criar um gráfico de barras com a contagem de cada status
grafico = sns.countplot(
    data=df,
    x='Status_Nutricional',
    hue='Status_Nutricional',
    palette='viridis',
    order=['Baixo Peso', 'Peso Normal', 'Sobrepeso', 'Obesidade']
)

# Colocar título e nomes nos eixos
plt.title('Distribuição do Status Nutricional (Amostra)', fontsize=14)
plt.xlabel('Categoria (OMS)', fontsize=12)
plt.ylabel('Número de Pacientes', fontsize=12)

# 5. Salvar o gráfico como imagem (Para usar no PDF depois!)
plt.tight_layout()
plt.savefig('grafico_imc.png', dpi=300)
print("\nGráfico salvo com sucesso como 'grafico_imc.png'!")

# Mostrar o gráfico na tela para você ver
plt.show()