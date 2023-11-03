lista_arquivos1 = ["IM0001.PDF", "IM0002.DCM", "IM0003.DCM", "IM0004.PDF", "IM0005.PDF"]
lista_arquivos2 = ["IM0001.PDF", "IM0002.DCM", "IM0004.PDF"]

arquivos_presentes = [arquivo for arquivo in lista_arquivos1 if arquivo in lista_arquivos2]
arquivos_faltando = [arquivo for arquivo in lista_arquivos1 if arquivo not in lista_arquivos2]

print(f"Arquivos presentes em ambos (sistema e backup): {', '.join(arquivos_presentes)}")
print(f"Total: {len(arquivos_presentes)}\n")

print(f"Arquivos faltando no sistema atual: {', '.join(arquivos_faltando)}")
print(f"Total: {len(arquivos_faltando)}")
