# 1. verificações iniciais
import os
import sqlite3

file_path = r'C:/Users/MeuPC/Documents/Data Science/projects/streaming-sql/data'
data_path = os.path.join(file_path, 'streaming_music.db')

conn = sqlite3.connect(data_path)
cursor = conn.cursor()

# 2. inserir dados
# na tabela Users
usuarios = [
    ('Dawid Podsiadlo', 'Premium', '2026-01-15'),
    ('Lucas Silveira', 'Free', '2026-02-10'),
    ('Tyler Joseph', 'Premium', '2026-03-05'),
    ('Yuma Nakakita', 'Free', '2026-04-01')
]
# aprendi: '?' são os espaços vazios que a lista vai preencher
cursor.executemany('INSERT INTO Users (nome, plano, data_cadastro) VALUES (?, ?, ?)', usuarios)

# na tabela Musicas
musicas = [
    ('March to the Sea', 'Twenty One Pilots', 'Rock', 332),
    ('Don\'t', 'Ed Sheeran', 'Pop', 220),
    ('To Love You More', 'Celine Dion', 'Pop', 279),
    ('Cancer', 'My Chemical Romance', 'Rock', 143),
    ('Coisas Que Eu Sei', 'Jorge Vercillo', 'MPB', 238),
    ('Od Nowa', 'Kwiat Jabloni', 'Pop', 229)
]
cursor.executemany('INSERT INTO Musicas (titulo, artista, genero, duracao_segundos) VALUES (?, ?, ?, ?)', musicas)

# na tabela Streams
# (id_user, id_musica, data_hora, completada)
streams = [
    (1, 1, '2026-04-05 10:00:00', 1),
    (2, 3, '2026-04-05 10:05:00', 0),
    (1, 2, '2026-04-05 10:10:00', 1),
    (3, 5, '2026-04-06 15:30:00', 1),
    (4, 4, '2026-04-07 08:00:00', 0),
    (2, 6, '2026-04-07 08:05:00', 1),
    (1, 5, '2026-04-07 09:00:00', 1)
]
cursor.executemany('INSERT INTO Streams (id_user, id_musica, data_hora, completada) VALUES (?, ?, ?, ?)', streams)

# salvar
conn.commit()
conn.close()

print("Dados injetados.")