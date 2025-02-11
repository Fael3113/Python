nome = input('Digite seu nome: ')
curso = input ('Digite seu curso: ')
nmatricula = input('Digite seu numero de matricula: ')
media = 0
for contador in range (1,5,1):
    nota = float(input(f'Insira a {contador}ª nota do aluno: '))
    media = media + nota 
    resultado = media/4
faltas = int(input('Digite o numero de faltas: '))
if resultado>=7:
    print('Aprovado')      
else:
    print('Reprovado')
print('Nome do Aluno:', nome)
print('Curso:', curso)
print('Numero da matricula:', nmatricula)
print('Sua media de notas é:{}'.format (resultado))
print('Seu numero de faltas é:', faltas)