import psycopg2

class Operacoes():

    def salvar(self, nome, matricula):
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

    def buscar(self):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="cesusc",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="banco_alunos")
            cursor = connection.cursor()
            select = "select * from aluno"
            cursor.execute(select)
            livros = cursor.fetchall()

            for row in livros:
                print("Id = ", row[0], )
                print("nome= ", row[1])
                print("matrícula = ", row[2], "\n")

        except(Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)
        finally:
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    def deletar(self, id_serial):
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





