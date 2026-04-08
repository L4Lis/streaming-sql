# 1. verificações iniciais
import os
import sqlite3
import pandas as pd

# configurar caminho
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'data')

if not os.path.exists(file_path):
    os.makedirs(file_path)

# criar e conectar ao banco de dados
data_path = os.path.join(file_path, 'streaming_music.db')
conn = sqlite3.connect(data_path)
cursor = conn.cursor()

# criar a tabela de Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (id_user INTEGER PRIMARY KEY, nome TEXT, plano TEXT, data_cadastro TEXT)
''')

# criando a tabela de Músicas
cursor.execute('''
CREATE TABLE IF NOT EXISTS Musicas (id_musica INTEGER PRIMARY KEY, titulo TEXT, artista TEXT, genero TEXT, duracao_segundos INTEGER)
''')

# criando a tabela de Streams
# coluna 'completada': se o user pulou a música ou ouviu até o fim. 1 True e 0 False.
cursor.execute('''
CREATE TABLE IF NOT EXISTS Streams (id_stream INTEGER PRIMARY KEY, id_user INTEGER, id_musica INTEGER, data_hora TEXT, completada BOOLEAN, FOREIGN KEY (id_user) REFERENCES Users (id_user), FOREIGN KEY (id_musica) REFERENCES Musicas (id_musica)
)
''')

# salvar arquivo
conn.commit()
conn.close()

print("Banco de dados criado.")