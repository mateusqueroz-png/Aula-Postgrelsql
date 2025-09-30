from db import conectar

def criar_aluno(nome,idade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO aluno (nome, idade) VALUES (%s, %s)",
                (nome, idade)
            )
            conexao.commit()
        except Exception as erro:
            print(f"erro ao inserir {erro}")
        finally:
            cursor.close()
            conexao.close()

def listar_aluno():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM aluno ORDER BY id"
            )
            return cursor.ferchall()
        except Exception as erro:
            print(f"erro ao inserir {erro}")
            return[]
        finally:
            cursor.close()
            conexao.close()

def atualizar_alunos(id_aluno, nova_idade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
            "UPDATE alunos SET idade = %s WHERE id = %s",
            (nova_idade, id_aluno)
            )
        except Exception as erro:
            print(f"Erro ao atualizar um aluno: {erro}")
        finally:
            cursor.close()
            conexao.close()

def deletar_aluno(id_aluno):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "DELETE FROM aluno WHERE id = %s", (id_aluno,)
            )
            conexao.commit()
        except Exception as erro:
            print(f"erro ao deletar aluno:")