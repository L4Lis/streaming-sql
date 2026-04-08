# 1. verificações iniciais
import sqlite3
import pandas as pd
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, 'data')
data_path = os.path.join(file_path, 'streaming_music.db')

conn = sqlite3.connect(data_path)

# 2. criar query de relatório geral
query_relatorio = """
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

# executar e exibir resultado do relatório geral
df_relatorio = pd.read_sql_query(query_relatorio, conn)

print("\n--- RELATÓRIO DE STREAMING ---")
print(df_relatorio.to_string(index=False))

# 4. criar query de ranking
query_ranking = """
SELECT 
    Musicas.artista AS Artista,
    COUNT(Streams.id_stream) AS Plays_Totais,
    SUM(Streams.completada) AS Plays_Ate_O_Fim
FROM Streams
JOIN Musicas ON Streams.id_musica = Musicas.id_musica
GROUP BY Musicas.artista
ORDER BY Plays_Totais DESC;
"""

# executar e exibir resultado do ranking
df_ranking = pd.read_sql_query(query_ranking, conn)

print("")
print("")
print("\n--- RANKING DE ARTISTAS ---")
print(df_ranking.to_string(index=False))

conn.close()