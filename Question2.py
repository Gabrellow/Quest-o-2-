# Solicita ao usuário que informe um número inteiro positivo
n = int(input("Digite um número inteiro positivo: "))

# Inicializa os dois primeiros termos da sequência de Fibonacci
fib_1 = 0
fib_2 = 1

# Inicializa uma variável para armazenar a soma dos dois termos anteriores
soma = 0

# Enquanto a soma dos dois termos anteriores for menor ou igual a n, calcule o próximo termo
while soma <= n:
    # Calcula o próximo termo da sequência de Fibonacci
    fib_atual = fib_1 + fib_2
    # Atualiza os valores dos dois termos anteriores
    fib_1 = fib_2
    fib_2 = fib_atual
    # Calcula a soma dos dois termos anteriores
    soma = fib_1 + fib_2

# Verifica se o número fornecido pertence ou não à sequência de Fibonacci
if soma == n or n == 0:
    print("O número fornecido pertence à sequência de Fibonacci.")
else:
    print("O número fornecido não pertence à sequência de Fibonacci.")