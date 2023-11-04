lista_arquivos1 = ["IM0001.PDF", "IM0002.DCM", "IM0003.DCM", "IM0004.PDF", "IM0005.PDF"]
lista_arquivos2 = ["IM0001.PDF", "IM0002.DCM", "IM0004.PDF"]


def comparacao(lista1, lista2):
    arquivos_presentes = [arquivo for arquivo in lista1 if arquivo in lista2]
    arquivos_faltando = [arquivo for arquivo in lista1 if arquivo not in lista2]
    return [arquivos_presentes, arquivos_faltando]


tabela_arquivos = comparacao(lista_arquivos1, lista_arquivos2)

print(f"Arquivos presentes em ambos (sistema e backup): {', '.join(tabela_arquivos[0])}")
print(f"Total: {len(tabela_arquivos[0])}\n")

print(f"Arquivos faltando no sistema atual: {', '.join(tabela_arquivos[1])}")
print(f"Total: {len(tabela_arquivos[1])}")
