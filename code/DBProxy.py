# Banco de Dados do projeto que armazena a pontuação dos jogadores após o fim do jogo

import sqlite3


class DBProxy:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.connection.execute('''
                                   CREATE TABLE IF NOT EXISTS dados(
                                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                                   name TEXT NOT NULL,
                                   score INTEGER NOT NULL,
                                   date TEXT NOT NULL)
                                '''
                                )
        
    # Função que salva a pontuação do jogador no banco de dados
    def save(self, score_dict: dict):
        self.connection.execute('INSERT INTO dados (name, score, date) VALUES (:name, :score, :date)', score_dict)
        self.connection.commit()
        
    # Função que recupera a pontuação do jogador no banco de dados
    def retrieve_top10(self) -> list:
        return self.connection.execute('SELECT * FROM dados ORDER BY score DESC LIMIT 10').fetchall()
        
    # Função que só fecha a conexão com o banco de dados
    def close(self):
        return self.connection.close()