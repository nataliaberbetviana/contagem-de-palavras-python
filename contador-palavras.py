with open('entrada.txt', 'r') as entrada:
    texto = entrada.read()

def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)

with open('saida.txt', 'w') as saida:
    saida.write(f'O número de palavras é: {contar_palavras(texto)}!')