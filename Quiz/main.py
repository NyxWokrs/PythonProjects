qtDePerguntas = int(input('Quantas Perguntas ?'))
perguntas = []
respostas = []
respostaCorreta = []
pontos = 0
for x in range(0,qtDePerguntas):
    perguntas.append(str(input('Escreva Sua Pergunta')))
    respostas.append(str(input('Escreve as alternativas (DE A - D)  para a pergunta feita')))
    respostaCorreta.append(str(input('DIGITE A RESPOSTA CORRETA')))
n=0
print('\n' * 10)
print('=' * 20 + 'INICIANDO QUIZ' + '=' * 20)
for question in perguntas:
    print(question)
    print(respostas[n])
    resposta = str(input('DIGITE A RESPOSTA :'))
    if resposta.lower() == respostaCorreta[n].lower():
        print('ACERTOU\n')
        pontos +=1
    else:
        print('ERROU\n')
    n +=1
print(f'VOCE ACERTOU {pontos} DE {len(perguntas)} !!')


