from fpdf import FPDF
import pandas as pd

df = pd.read_excel("projeto_nutricao_dados.xlsx")
df['IMC'] = df['Peso_kg'] / (df['Altura_m'] ** 2)

total_pacientes = len(df)
imc_medio = df['IMC'].mean()

class MeuPDF(FPDF):
    def header(self):
        # Fonte Arial (helvetica), Negrito (B), Tamanho 16
        self.set_font('helvetica', 'B', 16)
        # Título centralizado
        self.cell(0, 10, 'Relatório de Status Nutricional Automatizado', align='C', new_x="LMARGIN", new_y="NEXT")
        self.ln(5) # Pula uma linha

    def footer(self):
        # Rodapé com número da página
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', align='C')

#  Criar o documento
pdf = MeuPDF()
pdf.add_page()

pdf.set_font('helvetica', '', 12)
texto_introducao = (
    f"Este relatório apresenta a análise automatizada de {total_pacientes} pacientes.\n"
    f"O Índice de Massa Corporal (IMC) médio da amostra é de {imc_medio:.1f}.\n\n"
    "Abaixo, apresentamos a distribuição do status nutricional da amostra "
    "em comparação com os valores de referência da OMS."
)
pdf.multi_cell(0, 8, texto_introducao)
pdf.ln(5)

# w=160 define a largura da imagem no PDF
try:
    pdf.image('grafico_imc.png', w=160, keep_aspect_ratio=True)
except FileNotFoundError:
    print("Aviso: Imagem 'grafico_imc.png' não encontrada. Execute o script do gráfico primeiro!")

# Adicionar o "Espaço" para a assinatura do especialista 
pdf.ln(10)
pdf.set_font('helvetica', 'B', 12)
pdf.cell(0, 10, 'Recomendações Clínicas (Uso Exclusivo do Profissional de Saúde):', new_x="LMARGIN", new_y="NEXT")
pdf.set_font('helvetica', '', 10)
pdf.multi_cell(0, 8, "__________________________________________________________________________________\n"
                     "__________________________________________________________________________________\n"
                     "__________________________________________________________________________________")

nome_arquivo = "Relatorio_Final_Nutricao.pdf"
pdf.output(nome_arquivo)

print(f"\nSucesso absoluto! Abra o arquivo '{nome_arquivo}' na sua pasta para ver o resultado.")
