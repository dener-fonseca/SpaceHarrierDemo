# Módulo que cria e se comunica com banco de dados para salvar e carregar dados

import sqlite3


class DBProxy:
    # Método construtor para criar e conectar o programa a um banco de dados SQLite
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.connection.execute('''
                                   CREATE TABLE IF NOT EXISTS data(
                                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                                   name TEXT NOT NULL,
                                   score INTEGER NOT NULL,
                                   date TEXT NOT NULL)
                                '''
                                )

    # Método para salvar registros name, score, date
    def save(self, score_dict: dict):
        self.connection.execute('INSERT INTO data (name, score, date) VALUES (:name, :score, :date)', score_dict)
        self.connection.commit()

    # Método para retornar as 10 melhores pontuações
    def retrieve_top10(self) -> list:
        return self.connection.execute('SELECT * FROM data ORDER BY score DESC LIMIT 10').fetchall()

    # Método para fechar o banco de dados
    def close(self):
        return self.connection.close()