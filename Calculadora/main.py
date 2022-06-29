""""Criando uma calculadora:
1 - Escolher Função
2 - Adição
3 - Subtração
4 - Multiplicação
5 - Divisão
6 - Raiz Quadrada
7 - Elevar"""



from math import sqrt
print("1: Adição\n"
      "2: Subtração\n"
      "3: Multiplicação\n"
      "4: Divisão\n"
      "5: Raiz Quadrada\n"
      "6: Potência")
action = int(input('Qual ação deseja fazer ?'))

if action == 1: #ADIÇÃO
    resposta = ""
    resultado = 0
    somados = []
    while resposta != 0:
        numero = float(input('Digite o Valor:'))
        somados.append(numero)
        resultado = numero + resultado
        resposta = int(input("Deseja continuar 1:Sim 0:Não"))
    else:
        print(f"A Soma entre {somados} é de {resultado}")
        somados.clear()
elif action == 2:
    resposta = ""
    resultado = 0
    subtradios = []
    first = 0
    while resposta != 0:
        numero = float(input('Digite o Valor:'))
        subtradios.append(numero)
        if first == 0:
            resultado = numero
            first = numero
        else:
            resultado = resultado - numero
        resposta = int(input("Deseja continuar 1:Sim 0:Não"))
    else:
        print(f"A Subtração entre {subtradios} é de {resultado}")
        subtradios.clear()

elif action == 3:
    resposta = ""
    resultado = 1
    multiplicados = []
    while resposta != 0:
        numero = float(input('Digite o Valor:'))
        multiplicados.append(numero)
        resultado = numero * resultado
        resposta = int(input("Deseja continuar 1:Sim 0:Não"))
    else:
        print(f"O Produto entre {multiplicados} é de {resultado}")
        multiplicados.clear()
elif action == 4:
    resposta = ""
    resultado = 0
    divididos = []
    first = 0
    while resposta != 0:
        numero = float(input('Digite o Valor:'))
        divididos.append(numero)
        if first == 0:
            resultado = numero
            first = numero
        else:
            resultado = resultado / numero
        resposta = int(input("Deseja continuar 1:Sim 0:Não"))
    else:
        print(f"O Produto entre {divididos} é de {resultado}")
        divididos.clear()
elif action == 5:
    resposta = ""
    resultado = 1
    raizes = []
    first = 0
    while resposta != 0:
        numero = int(input('Digite o Valor:'))
        raizes.append(numero)
        if first == 0:
            first = numero
            resultado = sqrt(numero)
            resposta = 0
            print(f"A Raiz de {raizes} é de {resultado}")
            raizes.clear()
elif action == 6:
    resposta = ""
    resultado = 1
    elevados = []
    first = 0
    while resposta != 0:
        numero = float(input('Digite o Valor:'))
        elevados.append(numero)
        if first == 0:
            resultado = numero
            first = numero
        else:
            resultado = resultado ** numero
        resposta = int(input("Deseja continuar 1:Sim 0:Não"))
    else:
        print(f"A Potenciação de {elevados} é de {resultado}")
        elevados.clear()








