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

def potenciar(x, y):
    # Tratamento para evitar cálculos indefinidos ou estouro de limite
    try:
        resultado = x ** y
        # Se o resultado for complexo (ex: raiz par de número negativo)
        if isinstance(resultado, complex):
            return f"{resultado.real:.4f} + {resultado.imag:.4f}j (número complexo)"
        return resultado
    except ZeroDivisionError:
        return "Erro: zero não pode ser elevado a uma potência negativa!"
    except OverflowError:
        return "Erro: resultado muito grande para ser calculado!"

# 2. Função principal que gerencia o fluxo da calculadora
def calculadora():
    while True:
        print("\n=== CALCULADORA BÁSICA ===")
        print("1. Adição (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("5. Potenciação (^)")
        print("0. Sair")
        
        opcao = input("Escolha a operação (0-5): ")

        # Condição de saída do programa
        if opcao == "0":
            print("Obrigado por usar a calculadora. Até logo!")
            break

        # Validação da opção escolhida
        if opcao in ["1", "2", "3", "4", "5"]:
            try:
                # Conversão para float para suportar números decimais e inteiros
                num1 = float(input("Digite o primeiro número (ou base): "))
                num2 = float(input("Digite o segundo número (ou expoente): "))
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
            elif opcao == "5":
                resultado = potenciar(num1, num2)
                print(f"\nResultado: {num1} ^ {num2} = {resultado}")
        else:
            print("Opção inválida! Por favor, escolha um número de 0 a 5.")

# Ponto de entrada do script
if __name__ == "__main__":
    calculadora()