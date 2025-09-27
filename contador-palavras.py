# ============================================
# Definição da função para contar palavras
# ============================================
# A função 'def' cria um bloco de código reutilizável.
# Ela recebe um argumento chamado 'texto'.
def contar_palavras(texto):
    # O método .split() divide a string 'texto' em uma lista de palavras,
    # usando os espaços como separadores.
    palavras = texto.split()
    # A função len() conta o número de itens na lista 'palavras' e
    # 'return' retorna o resultado para quem chamou a função.
    return len(palavras)

# ============================================
# Lógica Principal do Script
# ============================================

# Abre o arquivo de entrada ('entrada.txt') no modo de leitura ('r').
# O 'with' garante que o arquivo seja fechado automaticamente.
with open('entrada.txt', 'r', encoding='utf-8') as entrada:
    # Lê todo o conteúdo do arquivo e armazena na variável 'texto'.
    texto = entrada.read()

# Chama a função 'contar_palavras' e passa o conteúdo do arquivo ('texto').
# O resultado da contagem é armazenado na variável 'total_de_palavras'.
total_de_palavras = contar_palavras(texto)

# Abre o arquivo de saída ('saida.txt') no modo de escrita ('w').
# Se o arquivo não existir, ele será criado. Se existir, será sobrescrito.
with open('saida.txt', 'w', encoding='utf-8') as saida:
    # Escreve a frase final no arquivo.
    # Usamos uma f-string para inserir o valor da contagem diretamente no texto.
    saida.write(f'O número de palavras é: {total_de_palavras}!')

# Imprime uma mensagem de sucesso no terminal.
print("Contagem de palavras concluída com sucesso se a contagem for de " + str(total_de_palavras) + " palavras!")