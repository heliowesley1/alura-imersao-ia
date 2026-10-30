# 1. Definição das funções para cada operação básica
def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    # Tratamento para evitar erro matemático de divisão por zero
    if y == 0:
        return "Erro: divisão por zero não é permitida!"
    return x / y

# 2. Função principal que gerencia o fluxo da calculadora
def calculadora():
    while True:
        print("\n=== CALCULADORA BÁSICA ===")
        print("1. Adição (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("0. Sair")
        
        opcao = input("Escolha a operação (0-4): ")

        # Condição de saída do programa
        if opcao == "0":
            print("Obrigado por usar a calculadora. Até logo!")
            break

        # Validação da opção escolhida
        if opcao in ["1", "2", "3", "4"]:
            try:
                # Conversão para float para suportar números decimais e inteiros
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Erro: Por favor, digite apenas números válidos.")
                continue

            # Executa a operação correspondente à escolha
            if opcao == "1":
                resultado = somar(num1, num2)
                print(f"\nResultado: {num1} + {num2} = {resultado}")
            elif opcao == "2":
                resultado = subtrair(num1, num2)
                print(f"\nResultado: {num1} - {num2} = {resultado}")
            elif opcao == "3":
                resultado = multiplicar(num1, num2)
                print(f"\nResultado: {num1} * {num2} = {resultado}")
            elif opcao == "4":
                resultado = dividir(num1, num2)
                print(f"\nResultado: {num1} / {num2} = {resultado}")
        else:
            print("Opção inválida! Por favor, escolha um número de 0 a 4.")

# Ponto de entrada do script
if __name__ == "__main__":
    calculadora()