import pandas as pd
from google import genai
import json

CHAVE_API = "AIzaSyC-oM31SZ9sa3QUdf8Zis9lQwdsvU8qlDM"
client = genai.Client(api_key=CHAVE_API)

df = pd.read_excel("projeto_nutricao_dados.xlsx")

def analisar_refeicao_com_ia(texto_dieta):
    prompt = f"""
    Aja como um software de análise nutricional. Analise o texto abaixo e estime os valores nutricionais totais.
    RETORNE APENAS UM OBJETO JSON VÁLIDO. Não inclua nenhuma outra palavra, saudação ou formatação markdown.

    Formato obrigatório do JSON:
    {{"calorias_kcal": int, "proteinas_g": int, "carboidratos_g": int, "gorduras_g": int}}

    Texto para analisar: "{texto_dieta}"
    """

    try:
        # Nova sintaxe do Google GenAI
        resposta = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )

        texto_limpo = resposta.text.replace('```json', '').replace('```', '').strip()
        dados_json = json.loads(texto_limpo)
        return dados_json

    except Exception as e:
        print(f"Erro ao processar: {texto_dieta} -> {e}")
        return {"calorias_kcal": 0, "proteinas_g": 0, "carboidratos_g": 0, "gorduras_g": 0}


print("Enviando dados para a IA (isso pode levar alguns segundos)...")

df_teste = df.head(3).copy()

resultados_ia = df_teste['Recordatorio_24h'].apply(analisar_refeicao_com_ia)

df_novas_colunas = pd.json_normalize(resultados_ia)
df_final = pd.concat([df_teste.reset_index(drop=True), df_novas_colunas], axis=1)

df_final.to_csv("dados_enriquecidos_ia.csv", index=False, encoding='utf-8-sig')

print("\nSucesso! Veja como ficou a tabela com as novas colunas:")
print(df_final[['Recordatorio_24h', 'calorias_kcal', 'proteinas_g']])
