# 1 - Criar lista de livros
livros = ["O Senhor dos Anéis", "Harry Potter", "Silêncio dos inocentes"]
print("Lista inicial de livros:", livros)

# 2 - Exibir primeiro e último livro
print("Primeiro livro:", livros[0])
print("Último livro:", livros[-1])

# 3 - Adicionar dois livros com append()
livros.append("1984")
livros.append("A Revolução dos Bichos")
print("Lista após append:", livros)

# 4 - Inserir "Duna" na segunda posição
livros.insert(1, "Duna")
print("Lista após inserir Duna:", livros)

# 5 - Remover "Silêncio dos inocentes" (com verificação)
if "Silêncio dos inocentes" in livros:
    livros.remove("Silêncio dos inocentes")
    print("Lista após remover Silêncio dos inocentes:", livros)
else:
    print("Livro não encontrado")

# 6 - Contar quantas vezes o número 2 aparece
numeros = [1, 2, 3, 2, 4, 2, 5]
print("O número 2 aparece", numeros.count(2), "vezes na lista.")

# 7 - Percorrer a lista de livros
for livro in livros:
    print(f"O livro {livro} é interessante")

# 8 - Exibir idades maiores ou iguais a 18
idades = [12, 18, 25, 14, 30]
print("Idades maiores ou iguais a 18:")
for idade in idades:
    if idade >= 18:
        print(idade)

# 9 - Somar manualmente a lista de valores
valores = [10, 20, 30, 40]
soma = 0
for v in valores:
    soma += v
print("Soma dos valores:", soma)

# 10 - Receber notas de 2 alunos
notas = []
for i in range(2):
    aluno_notas = []
    print(f"Digite as 3 notas do aluno {i+1}:")
    for j in range(3):
        nota = float(input(f"Nota {j+1}: "))
        aluno_notas.append(nota)
    notas.append(aluno_notas)

# Calcular média de cada aluno
for i, aluno_notas in enumerate(notas):
    media = sum(aluno_notas) / len(aluno_notas)
    print(f"Média do aluno {i+1}: {media:.2f}")

# 11 - Tabuleiro de xadrez com peças iniciais
# Criar tabuleiro vazio
tabuleiro = [["[ ]" for _ in range(8)] for _ in range(8)]

# Peças brancas
tabuleiro[0] = ["tor", "cav", "bis", "rai", "rei", "bis", "cav", "tor"]
tabuleiro[1] = ["pea"] * 8

# Peças pretas
tabuleiro[6] = ["pea"] * 8
tabuleiro[7] = ["tor", "cav", "bis", "rai", "rei", "bis", "cav", "tor"]

# Imprimir tabuleiro
print("\nTabuleiro de xadrez inicial:")
for linha in tabuleiro:
    print(" ".join(linha))
