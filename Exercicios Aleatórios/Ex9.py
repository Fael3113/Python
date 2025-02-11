#Sistema Simples de Controle de Notas e Faltas
def criarAluno(nome, RA, curso):
    aluno = {
        'nome' : nome,
        'RA' : RA,
        'curso' : curso,
        # o elemento abaixo é um agrupamento da nota total que o aluno tirou em uma disciplina
        'notas' : {}, # 'disciplina' : nota (coloque sempre números reais, mesmo que o número seja inteiro, bote o ponto)
        # o elemento abaixo é um agrupamento das faltas totais que um aluno teve em uma disciplina
        'faltas' : {} # 'disciplina' : falta (sempre número inteiro)
    }
    return aluno

def darNota(aluno, disciplina, nota):
    # Verifica se a disciplina já está registrada nas notas do aluno
    if disciplina in aluno['notas']:
        aluno['notas'][disciplina] += nota
    else:
        aluno['notas'][disciplina] = nota

def darFaltaEmUmaDisciplina(aluno, disciplina):
    # Verifica se a disciplina já está registrada nas faltas do aluno
    if disciplina in aluno['faltas']:
        aluno['faltas'][disciplina] += 1
    else:
        aluno['faltas'][disciplina] = 1

def calcMediaNotas(aluno):
    # Verifica se há notas registradas
    if aluno['notas'] == {}:
        return 0.0  # Sem notas registradas
    # Calcula a média das notas
    else:
        notas = aluno['notas']
        total = sum(notas.values())
        media = (total) / len(notas)
        return media

def calcTotalFaltas(aluno):
    return sum(aluno['faltas'].values())

def verificarAprovacao(aluno):
    media = calcMediaNotas(aluno)
    if media >= 7.0:
        return True
    else:
        return False


# SISTEMA PRINCIPAL

alunos = []

while True:
    print('0 - Parar CRUD')
    print('1 - Cadastrar alunos')
    print('2 - Registrar nota')
    print('3 - Registrar falta')
    opcao = int(input('Selecione uma das opções acima: '))
    try:
        if opcao == 0:
            break
        elif opcao == 1:
            nome = str(input('Insira o nome do aluno: '))
            RA = str(input('Insira o RA do aluno: '))
            curso = str(input('Insira o curso do aluno: '))
            aluno = criarAluno(nome, RA, curso)
            alunos.append(aluno)
        elif opcao == 2:
            for c in range(0, len(alunos), 1):
                print(f'{c} - {alunos[c]}\n')
            opcao_aluno = int(input('Selecione um dos alunos acima pelo número: '))
            aluno = alunos[opcao_aluno]
            disciplina = str(input('Insira a disciplina: '))
            nota = float(input('Insira a nota: '))
            darNota(aluno, disciplina, nota)
        elif opcao == 3:
            for c in range(0, len(alunos), 1):
                print(f'{c} - {alunos[c]}\n')
            opcao_aluno = int(input('Selecione um dos alunos acima pelo número: '))
            aluno = alunos[opcao_aluno]
            disciplina = str(input('Insira a disciplina a qual deseja adicionar uma falta do aluno: '))
            darFaltaEmUmaDisciplina(aluno, disciplina)
    except Exception:
        print('Opção inválida!')
        continue

# Cria lista de aprovados e reprovados
alunos_statusAprovacao = []
for c in range(0, len(alunos), 1):
    alunos_statusAprovacao.append(verificarAprovacao(alunos[c]))
# O Id do aluno na lista de alunos será o mesmo aqui
# Então basta usar o Id do aluno nesta lista para saber se foi aprovado ou não

# Cria lista com o total de faltas de cada aluno
alunos_TotalFaltas = []
for c in range(0, len(alunos), 1):
    alunos_TotalFaltas.append(calcTotalFaltas(alunos[c]))
# O Id do aluno na lista de alunos será o mesmo aqui
# Então basta usar o Id do aluno nesta lista para saber o total de faltas do aluno específico

print('RELATÓRIO DE DESEMPENHO')
for c in range(0, len(alunos), 1):
    print(f'ID do aluno no sistema: {c}')
    print(f"    Nome do aluno: {alunos[c]['nome']}")
    print(f"    RA do aluno: {alunos[c]['RA']}")
    print(f"    Curso do aluno: {alunos[c]['curso']}")
    print("    NOTAS:")
    for materia, nota in alunos[c]['notas'].items():
        print(f"        Nota total em {materia}: {nota}")
    print(f"    Média global do aluno: {format(calcMediaNotas(alunos[c]), '.2f')}")
    print("    FALTAS:")
    for materia, faltas in alunos[c]['faltas'].items():
        print(f"        Faltas em {materia}: {faltas}")
    print(f"    Total de faltas: {alunos_TotalFaltas[c]}")
    if alunos_statusAprovacao[c] == True:
        print("    Status de aprovação: aprovado")
    else:
        print("    Status de aprovação: reprovado")
