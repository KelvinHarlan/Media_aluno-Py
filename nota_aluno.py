'''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.'''

nota_1 = float(input('Digite uma nota entre 0 e 10\n'))
nota_2 = float(input('Digite a segunda nota entre 0 e 10\n'))
media = (nota_1+nota_2)/2
if media >=0 and media < 7:
    print(f'Ola, sua nota foi {media}, você está Reprovado!\n')
elif media >= 7 and media <=9:
    print(f'Ola, sua nota foi {media}, você está Aprovado!\n')
elif media == 10:
    print(f'Ola, sua nota foi {media}, você foi Aprovado com nota máxima!\n')