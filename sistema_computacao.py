#ALUNO: CAIO CESAR PASCHOAL TAVARES
def conversao():
    while True:
        print("\n=== Calculadora de Conversão ===")
        print("1 - Inserir número Decimal")
        print("2 - Inserir número Binário")
        print("3 - Inserir número Octal")
        print("4 - Inserir número Hexadecimal")
        print("5 - Sair")

        opcao = int(input("Digite a opção de 1 - 5: "))

        if opcao == 1:
            numero = int(input("Digite o número decimal: "))
            print("\033[91mDecimal:", numero, "\033[0m")
            print("\033[91mBinário:", bin(numero)[2:], "\033[0m")
            print("\033[91mOctal:", oct(numero)[2:], "\033[0m")
            print("\033[91mHexadecimal:", hex(numero)[2:].upper(), "\033[0m")

        elif opcao == 2:
            numero = input("Digite o número binário: ")
            dec = int(numero, 2)
            print("\033[91mBinário:", numero, "\033[0m")
            print("\033[91mDecimal:", dec, "\033[0m")
            print("\033[91mOctal:", oct(dec)[2:], "\033[0m")
            print("\033[91mHexadecimal:", hex(dec)[2:].upper(), "\033[0m")

        elif opcao == 3:
            numero = input("Digite o número octal: ")
            dec = int(numero, 8)
            print("\033[91mOctal:", numero, "\033[0m")
            print("\033[91mDecimal:", dec, "\033[0m")
            print("\033[91mBinário:", bin(dec)[2:], "\033[0m")
            print("\033[91mHexadecimal:", hex(dec)[2:].upper(), "\033[0m")

        elif opcao == 4:
            numero = input("Digite o número hexadecimal: ")
            dec = int(numero, 16)
            print("\033[91mHexadecimal:", numero.upper(), "\033[0m")
            print("\033[91mDecimal:", dec, "\033[0m")
            print("\033[91mBinário:", bin(dec)[2:], "\033[0m")
            print("\033[91mOctal:", oct(dec)[2:], "\033[0m")

        elif opcao == 5:
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Por favor, digite um número de 1 a 5.")

# Executa a função
conversao()