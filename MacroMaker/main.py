import keyboard,time


macros = [] # Pega os macros ja feitos
tempos = []

teclas = [] # Teclas pressionadas para criar um macro
teclasPressionadas = []

tempTempos = []

gatilho = str(input('Digite a tecla de gatilho'))
continuar = 's'

actualKey = 0
actualTime = 0
tempClicked = 0
while continuar == 's':
    teclas.append(input('Digite a tecla'))
    tempTempos.append(float(input('Digite o tempo para a proxima tecla')))
    continuar = str(input('QUER CONTIUNAR S / N')).lower()
    if continuar == 'n':
        tempos.append(tempTempos.copy())
        macros.append(teclas.copy())
        tempTempos.clear()
        teclas.clear()
        f = open('MACROS.txt','a')
        f.write(str(macros))
        f.write('\n')
        f.write(str(tempos))

while continuar == 'n':
    if keyboard.is_pressed(gatilho) and tempClicked == 0:
        if actualKey == 0:
            for macro in macros:
                for realMacro in macro:
                    actualKey = realMacro
                    if len(actualKey) < 2:
                        keyboard.press(actualKey)
                        teclasPressionadas.append(actualKey)
                    else:
                        print('ola')
                        if actualKey == 'end' or actualKey == 'up':
                            keyboard.press(actualKey)
                            teclasPressionadas.append(actualKey)
                        if actualKey == 'esc' or actualKey == 'enter':
                            keyboard.send(actualKey)
                            teclasPressionadas.append(actualKey)
                        else:

                            keyboard.write(actualKey)
                    time.sleep(tempos[0][actualTime])
                    actualTime +=1
                    tempClicked = 5000


    if tempClicked > 0:
        tempClicked -=1
    if tempClicked == 0:
        if actualKey !=0:
            print(teclasPressionadas)
            for key in teclasPressionadas:
                if len(key) < 2:
                    print(key)
                    keyboard.release(key)
            teclasPressionadas.clear()
            actualKey = 0
            actualTime = 0







#Fazer o programa ler o macro
#Fazer multiplos macros a partir dos triggers
