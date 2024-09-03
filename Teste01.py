#  Função para calcular a sequência de Fibonacci.
def calcFibonacci(num):
    if num < 0:
        return False
    
    a, b = 0, 1
    
    while a < num:
        a, b = b, a + b

    return a == num
# Essa função vai validar o número, para caso o usuário digite números do tipo float/negativo ou caracteres.
def validateNum():
    while True:
        #Coloquei um input para que ao rodar o código o usuário informe um número no terminal.
        user_input = input("Digite um número: ")
        try:
            number = int(user_input)
            if number >= 0:
                return number
            else:
                print("Por favor, insira um número válido.")
        except ValueError:
            print("Erro: o número digitado não é válido.")


numero = validateNum()

if calcFibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci!")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci!")
