import PyPDF2
import os

merger = PyPDF2.PdfMerger()

lista = os.listdir('arquivos')
lista.sort()
print(lista)

for arquivo in lista:
    if ".pdf" in arquivo:
        merger.append(f"arquivos/{arquivo}")
pdf_final = "PDF COMPLETO.pdf"
merger.write(pdf_final)
merger.close()

print(" ")
print("==============================================")
print("               Mesclador de PDF               ")
print("==============================================")
print("PDFs mesclados com sucesso!")
print("PDFs mesclados : {}".format(lista))
print("PDF Final: {}".format(pdf_final))
print("==============================================")
print(" ")