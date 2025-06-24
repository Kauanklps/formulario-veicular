import sqlite3

def init_db():
    conn = sqlite3.connect('instance/database.db')
    cursor = conn.cursor()

    # Criação da tabela de checklist de verificações
    conn.execute('''
    CREATE TABLE IF NOT EXISTS checklist (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        colaborador TEXT NOT NULL,
        veiculo TEXT NOT NULL,
        quilometragem INTEGER NOT NULL,
        ultima_validacao TEXT NOT NULL,
        oleo TEXT NOT NULL,
        freio TEXT NOT NULL,
        aditivo TEXT NOT NULL,
        pneus TEXT NOT NULL,
        observacoes TEXT,
        data TEXT NOT NULL
    )
''')

    conn.commit()
    conn.close()
    print("Banco de dados inicializado com sucesso.")

if __name__ == "__main__":
    init_db()
