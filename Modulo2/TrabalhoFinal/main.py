from menus import *
from funcoes import *

def main():
    while True:
        menu_principal()
        op = input("Opção: ")
        if op == "1":
            while True:
                menu_alunos()
                o = input("Opção: ")
                if o == "1":
                    cadastrar_aluno()
                elif o == "2":
                    print("\n=== LISTA DE ALUNOS ===")
                    for a in alunos:
                        print(a)
                elif o == "0":
                    break
                else:
                    print("Opção inválida!")
        elif op == "2":
            while True:
                menu_professores()
                o = input("Opção: ")
                if o == "1":
                    cadastrar_professor()
                elif o == "2":
                    print("\n=== LISTA DE PROFESSORES ===")
                    for p in professores:
                        print(p)
                elif o == "0":
                    break
                else:
                    print("Opção inválida!")
        elif op == "3":
            while True:
                menu_disciplinas()
                o = input("Opção: ")
                if o == "1":
                    cadastrar_disciplina()
                elif o == "2":
                    print("\n=== LISTA DE DISCIPLINAS ===")
                    for d in disciplinas:
                        print(d)
                elif o == "0":
                    break
                else:
                    print("Opção inválida!")
        elif op == "4":
            while True:
                menu_turmas()
                o = input("Opção: ")
                if o == "1":
                    cadastrar_turma()
                elif o == "2":
                    print("\n=== LISTA DE TURMAS ===")
                    for t in turmas:
                        print(t)
                elif o == "3":
                    inserir_aluno_turma()
                elif o == "4":
                    print("\n=== ALUNOS POR TURMA ===")
                    for t in turmas:
                        print(f"\n{t.nome}:")
                        print(t.listar_alunos())
                elif o == "0":
                    break
                else:
                    print("Opção inválida!")
        elif op == "5":
            inserir_aluno_turma()
        elif op == "6":
            lancar_notas()
        elif op == "7":
            exibir_resultados()
        elif op == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")
main()