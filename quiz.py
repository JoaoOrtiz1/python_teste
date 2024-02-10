import re
import random


def ola_mundo():
    print("Olá, mundo!")

def calcular_media():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))
    media = (num1 + num2 + num3) / 3
    print("A média é:", media)

def contar_palavras_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            palavras = conteudo.split()
            num_palavras = len(palavras)
            print(f"O arquivo '{nome_arquivo}' possui {num_palavras} palavras.")
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")

def converter_temperatura():
    escolha = input("Escolha a conversão (C para Celsius, F para Fahrenheit): ").upper()
    if escolha == 'C':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} Fahrenheit é igual a {celsius:.2f} Celsius.")
    elif escolha == 'F':
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} Celsius é igual a {fahrenheit:.2f} Fahrenheit.")
    else:
        print("Escolha inválida. Por favor, escolha C ou F.")

def jogo_da_forca():
    def escolher_palavra():
        palavras = ["python", "java", "javascript", "html", "css", "php", "ruby", "csharp", "swift", "kotlin"]
        return random.choice(palavras)

    def exibir_forca(erros):
        forca = [
            """
            ------
            |    |
            |
            |
            |
            |
            -
            """,
            """
            ------
            |    |
            |    O
            |
            |
            |
            -
            """,
            """
            ------
            |    |
            |    O
            |    |
            |
            |
            -
            """,
            """
            ------
            |    |
            |    O
            |   /|
            |
            |
            -
            """,
            """
            ------
            |    |
            |    O
            |   /|\\
            |
            |
            -
            """,
            """
            ------
            |    |
            |    O
            |   /|\\
            |   /
            |
            -
            """,
            """
            ------
            |    |
            |    O
            |   /|\\
            |   / \\
            |
            -
            """
        ]
        return forca[erros]

    def jogar_forca():
        palavra_secreta = escolher_palavra()
        palavra_oculta = ["_"] * len(palavra_secreta)
        letras_erradas = []
        tentativas_maximas = 6
        tentativas = 0

        print("Bem-vindo ao Jogo da Forca!")
        print("A palavra tem", len(palavra_secreta), "letras.")

        while True:
            letra = input("Digite uma letra: ").lower()

            if letra.isalpha() and len(letra) == 1:
                if letra in palavra_secreta:
                    for i in range(len(palavra_secreta)):
                        if palavra_secreta[i] == letra:
                            palavra_oculta[i] = letra
                    print("Palavra: " + " ".join(palavra_oculta))
                else:
                    letras_erradas.append(letra)
                    tentativas += 1
                    print(exibir_forca(tentativas))
                    print("Letras erradas:", " ".join(letras_erradas))

                if "_" not in palavra_oculta:
                    print("Parabéns! Você venceu. A palavra era:", palavra_secreta)
                    break

                if tentativas == tentativas_maximas:
                    print("Você perdeu! A palavra era:", palavra_secreta)
                    break
            else:
                print("Por favor, digite uma única letra válida.")

    if __name__ == "__main__":
        jogar_forca()


def listar_arquivos_pasta_atual():
    import os
    arquivos_pasta_atual = os.listdir()
    print("Arquivos e pastas no diretório atual:")
    for arquivo in arquivos_pasta_atual:
        print(arquivo)

def capturar_excecao_divisao_zero():
    try:
        numerador = int(input("Digite o numerador: "))
        denominador = int(input("Digite o denominador: "))
        resultado = numerador / denominador
        print("Resultado:", resultado)
    except ZeroDivisionError:
        print("Erro: Divisão por zero não permitida.")
    except ValueError:
        print("Erro: Certifique-se de inserir números inteiros.")

def operacoes_matematicas():
   def adicao(a, b):
    return a + b

    def subtracao(a, b):
        return a - b

    def multiplicacao(a, b):
        return a * b

    def divisao(a, b):
        if b != 0:
            return a / b
        else:
            return "Erro: Divisão por zero não é permitida."

    def potenciacao(a, b):
        return a ** b

    def realizar_operacao():
        print("Escolha a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Potenciação")

        escolha = input("Digite o número da operação desejada: ")

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            if escolha == '1':
                resultado = adicao(num1, num2)
            elif escolha == '2':
                resultado = subtracao(num1, num2)
            elif escolha == '3':
                resultado = multiplicacao(num1, num2)
            elif escolha == '4':
                resultado = divisao(num1, num2)
            elif escolha == '5':
                resultado = potenciacao(num1, num2)
            else:
                print("Escolha inválida. Por favor, escolha um número de 1 a 5.")
                return

            print(f"Resultado: {resultado}")

        except ValueError:
            print("Erro: Certifique-se de inserir números válidos.")

    if __name__ == "__main__":
        realizar_operacao()


def validar_email(email):
    padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(padrao, email):
        print(f"{email} é um endereço de e-mail válido.")
    else:
        print(f"{email} não é um endereço de e-mail válido.")

def encontrar_primo_intervalo():
    def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

    def encontrar_primos_no_intervalo(inicio, fim):
        primos = []
        for num in range(inicio, fim + 1):
            if eh_primo(num):
                primos.append(num)
        return primos

    if __name__ == "__main__":
        try:
            inicio = int(input("Digite o início do intervalo: "))
            fim = int(input("Digite o fim do intervalo: "))

            if inicio < 0 or fim < 0 or inicio > fim:
                raise ValueError("Intervalo inválido. Certifique-se de que o início seja menor que o fim.")

            numeros_primos = encontrar_primos_no_intervalo(inicio, fim)

            if numeros_primos:
                print(f"Números primos no intervalo de {inicio} a {fim}: {numeros_primos}")
            else:
                print(f"Nenhum número primo encontrado no intervalo de {inicio} a {fim}.")
        except ValueError as ve:
            print(f"Erro: {ve}")


## faça aki as chamadas das functions
validar_email('email@gmail.com')
##