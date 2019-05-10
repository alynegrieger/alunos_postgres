import psycopg2
from operacoes_banco import Operacoes

class Aluno(Operacoes):

    def  salvar(self):
        nome = input("Nome: ")
        matricula = input("Matrícula: ")
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="cesusc",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="banco_alunos")
            cursor = connection.cursor()
            insert = """insert into aluno (nome, matricula) values ('{0}', '{1}');""".format(nome, matricula)

            cursor.execute(insert)
            connection.commit()
            print("Aluno inserido com sucesso ")
        except(Exception, psycopg2.DatabaseError) as error:
            print("Error", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    def deletar(self):
        id_serial = input("Digite o ID: ")
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="cesusc",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="banco_alunos")
            cursor = connection.cursor()
            delete = "delete from aluno where id = {0} ".format(id_serial)
            cursor.execute(delete)
            connection.commit()
            print("Id {} deletado com sucesso: ".format(id_serial))
        except(Exception, psycopg2.Error) as error:
            print("Error while deleting from PostgreSQL", error)
        finally:
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    def menu(self):
        opcao = None

        while opcao != 0:
            opcao = int(input("[1] - Cadastrar aluno [2] - Listar alunos [3] - Deletar aluno  [0] - Sair: "))

            if opcao == 1:
                aluno = Aluno()
                aluno.salvar()
            elif opcao == 2:
                aluno = Aluno()
                aluno.buscar()
            elif opcao == 3:
                aluno = Aluno()
                aluno.deletar()
            elif opcao == 0:
                break



