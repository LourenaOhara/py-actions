from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, PageBreak, Image, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
import pandas as pd
import math

df = pd.read_csv('wwII-events.csv', sep=";")
df_data = [df.columns[:,].values.astype(str).tolist()] + df.values.tolist()
pg_data = df_data[1:]

##numero de paginas do PDF
# numero registros por pagina
#total de paginas
elements = []
rec_pg = 20 
total_pg = math.ceil(len(df_data)/rec_pg)

##estilo e template do PDF
styles = getSampleStyleSheet()
doc = SimpleDocTemplate('csv_to_pdf', rightMargin=0, leftMargin=0, topMargin=0, bottomMargin=0)

#cabecalho
def createPageHeader():
    elements.append(Spacer(1,10))
    elements.append(Image('war.jpeg', 100, 25))
    elements.append(Paragraph("Segunda Guerra Mundial - Eventos", styles['Title']))
    elements.append(Spacer(1,8))

#paginacao
def paginatePDF(start, stop):
    tbl = Table(df_data[0:1] + pg_data[start:stop])  
    tbl.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), '#F5F5F5'),
                              ('FONTSIZE', (0, 0), (-1, 0), 8),
                              ('GRID', (0, 0), (-1, -1), .5, '#a7a5a5')])) 
    elements.append(tbl)

##gerar PDF
def generatePDF():
    cur_pg = 0
    start_pos = 0
    stop_pos = rec_pg

    for cur_pg in range(total_pg):
        createPageHeader()
        paginatePDF(start_pos, stop_pos)
        elements.append(PageBreak())
        start_pos += rec_pg
        stop_pos += rec_pg
    doc.build(elements)

generatePDF()
print("PDF gerado com sucesso.")