import psycopg2
from dotenv import load_dotenv
import os

#Carregar variáveis do .env
params ={
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "host": os.getenv("DB_HOST"),
    "port": os .getenv("DB_PORT"),
}
def conectar():
    try:
        conexao = pg.connect(**params)
        cursor = conexao.cursor()
        return conexao, cursor
    except Exception as erro:
        print(f"Erro de conexao{erro}")
        return None, None