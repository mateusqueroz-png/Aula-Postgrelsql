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

