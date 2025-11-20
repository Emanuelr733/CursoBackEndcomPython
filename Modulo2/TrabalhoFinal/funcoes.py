from classes import Aluno, Professor, Disciplina, Turma, NotaInvalidaError
alunos = []
professores = []
disciplinas = []
turmas = []

def cadastrar_aluno():
    print("\n=== Cadastro de Aluno ===")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    nasc = input("Data nascimento (dd/mm/aaaa): ")
    matricula = input("Matrícula: ")
    curso = input("Curso: ")
    aluno = Aluno(nome, cpf, nasc, matricula, curso)
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!")

def cadastrar_professor():
    print("\n=== Cadastro de Professor ===")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    nasc = input("Data nascimento (dd/mm/aaaa): ")
    try:
        salario = float(input("Salário: "))
    except ValueError:
        print("Salário inválido.")
        return
    prof = Professor(nome, cpf, nasc, salario)
    professores.append(prof)
    print("Professor cadastrado!")

def cadastrar_disciplina():
    print("\n=== Cadastro de Disciplina ===")
    nome = input("Nome disciplina: ")
    try:
        carga = int(input("Carga horária: "))
    except ValueError:
        print("Carga horária inválida.")
        return
    if not professores:
        print("Nenhum professor cadastrado!")
        return
    print("\nSelecione o professor:")
    for i, p in enumerate(professores):
        print(f"{i} - {p.nome}")
    try:
        idx = int(input("Professor: "))
        professor = professores[idx]
    except (ValueError, IndexError):
        print("Opção inválida!")
        return
    disc = Disciplina(nome, carga, professor)
    disciplinas.append(disc)
    print("Disciplina cadastrada!")

def cadastrar_turma():
    print("\n=== Cadastro de Turma ===")
    nome = input("Nome da turma: ")
    if not disciplinas:
        print("Nenhuma disciplina cadastrada!")
        return
    print("\nSelecione a disciplina:")
    for i, d in enumerate(disciplinas):
        print(f"{i} - {d.nome}")
    try:
        idx = int(input("Disciplina: "))
        disc = disciplinas[idx]
    except (ValueError, IndexError):
        print("Opção inválida!")
        return
    turma = Turma(nome, disc)
    turmas.append(turma)
    print("Turma criada!")

def inserir_aluno_turma():
    print("\n=== Inserir Aluno na Turma ===")
    if not alunos or not turmas:
        print("Cadastre alunos e turmas antes.")
        return
    print("Selecione o aluno:")
    for i, a in enumerate(alunos):
        print(f"{i} - {a.nome}")
    try:
        idx_a = int(input("Aluno: "))
        aluno = alunos[idx_a]
    except (ValueError, IndexError):
        print("Aluno inválido!")
        return
    print("Selecione a turma:")
    for i, t in enumerate(turmas):
        print(f"{i} - {t.nome}")
    try:
        idx_t = int(input("Turma: "))
        turma = turmas[idx_t]
    except (ValueError, IndexError):
        print("Turma inválida!")
        return
    if aluno in turma.alunos:
        print("Este aluno já está na turma!")
        return
    turma.adicionar_aluno(aluno)
    print("Aluno adicionado à turma!")

def lancar_notas():
    print("\n=== Lançamento de Notas ===")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    print("Escolha o aluno:")
    for i, a in enumerate(alunos):
        print(f"{i} - {a.nome}")
    try:
        idx = int(input("Aluno: "))
        aluno = alunos[idx]
    except (ValueError, IndexError):
        print("Aluno inválido!")
        return
    try:
        nota = float(input("Nota (0 a 10): "))
        aluno.adicionar_nota(nota)
        print("Nota lançada!")
    except ValueError:
        print("Valor inválido.")
    except NotaInvalidaError as e:
        print("Erro:", e)

def exibir_resultados():
    print("\n=== RESULTADOS ===")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    for a in alunos:
        media = a.calcular_media()
        print(f"{a.nome} | Média: {media:.2f} | Situação: {a.situacao()}")