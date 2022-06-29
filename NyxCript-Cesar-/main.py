import random
from time import sleep

caracteres = [' ','q','Q','w','W','e','E','r','R','t','T','y','Y','u','U','i','I','o','O','p','P','a','A','s','S','d','D','f','F','g','G','h','H','j','J','K','k','L','l','ç','Ç','z','Z','X','x','C','c','v','V','b','B','n','N','m','M','1','2','3','4','5','6','7','8','9','0']
caracteresList = [] # Lista de letras no texto
caracteresCripto = [] #lISTA DE LETRAS CRIPTOGRAFADAS
action = input('Cripto or Uncripto')
key = 4
def cripto(text):
    global realText,caracteresCripto
    text = f.readlines()
    for line in text:
        for caracter in line:
            caracteresList.append(caracter) # Salva todas as letras do texto
    for caracter in caracteresList:
        if caracter == '0' or caracter == '9' or caracter == '8' or caracter == '7' or caracter == '6':
            caracter = caracteres.index(caracter) - key  # Faz a criptografia
            caracteresCripto.append(caracteres[caracter])
        else:
            caracter = caracteres.index(caracter) + key # Faz a criptografia
            caracteresCripto.append(caracteres[caracter])


    with open('text.txt', 'w') as d:
        d.write('')

    for letter in caracteresCripto:
        with open('text.txt', 'a') as t:
            t.writelines(letter)
            print(letter)




def uncripto(text):
    global caracteres
    carc = ''
    text = f.readlines()
    for line in text:
        for letter in line:
            if letter == '6' or letter == '5' or letter == '4' or letter == '3' or letter == '2':
                carc = caracteres.index(letter) + key
                print(caracteres[carc])
            else:
                carc = caracteres.index(letter) - key
                print(caracteres[carc])

        while True:
            sleep(1)


if action == 'Cripto':
    with open('text.txt', 'w') as f:
        f.write(str(input('Digite o texto a ser criptografado: ')))
    with open('text.txt') as f:
        cripto(f)
else:
    with open('text.txt') as f:
        uncripto(f)
