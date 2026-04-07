# 1. verificações iniciais
import sqlite3
import pandas as pd
import os

file_path = r'C:/Users/MeuPC/Documents/Data Science/projects/streaming-sql/data'
data_path = os.path.join(file_path, 'streaming_music.db')

conn = sqlite3.connect(data_path)

# 2. criar query
# utilizar JOIN para ter Usuário e Música juntos, e CASE para mostrar se o usuário ouviu a música até o fim ou pulou.
query = """
SELECT 
    Users.nome AS Usuario,
    Musicas.titulo AS Musica,
    Musicas.artista AS Artista,
    Streams.data_hora AS Horario,
    CASE 
        WHEN Streams.completada = 1 THEN 'Sim' 
        ELSE 'Não (Pulou)' 
    END AS Ouviu_Ate_O_Fim
FROM Streams
JOIN Users ON Streams.id_user = Users.id_user
JOIN Musicas ON Streams.id_musica = Musicas.id_musica;
"""

# 3. executar e exibir resultado
df_relatorio = pd.read_sql_query(query, conn)

print("\n--- RELATÓRIO DE STREAMING ---")
print(df_relatorio.to_string(index=False))

conn.close()