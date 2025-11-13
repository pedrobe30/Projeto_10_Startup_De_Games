import sqlite3
from datetime import datetime



conn = sqlite3.connect('game_database.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS Inventario;")
cursor.execute("DROP TABLE IF EXISTS Personagens;")
cursor.execute("DROP TABLE IF EXISTS Itens;")
cursor.execute("DROP TABLE IF EXISTS Jogadores;")


cursor.execute("""
CREATE TABLE Jogadores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nickname TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    data_criacao TEXT NOT NULL
);
""")


cursor.execute("""
CREATE TABLE Personagens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    classe TEXT NOT NULL,
    nivel INTEGER NOT NULL,
    jogador_id INTEGER NOT NULL,
    FOREIGN KEY (jogador_id) REFERENCES Jogadores (id)
);
""")


cursor.execute("""
CREATE TABLE Itens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT UNIQUE NOT NULL,
    tipo TEXT NOT NULL,
    valor INTEGER NOT NULL
);
""")


cursor.execute("""
CREATE TABLE Inventario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    personagem_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    FOREIGN KEY (personagem_id) REFERENCES Personagens (id),
    FOREIGN KEY (item_id) REFERENCES Itens (id)
);
""")

conn.commit()


data_hoje = datetime.now().strftime("%Y-%m-%d")
cursor.executemany("""
INSERT INTO Jogadores (nickname, email, data_criacao)
VALUES (?, ?, ?);
""", [
    ("HeroMaster", "hero@pixelverse.com", data_hoje),
    ("ShadowQueen", "shadow@pixelverse.com", data_hoje)
])


cursor.executemany("""
INSERT INTO Personagens (nome, classe, nivel, jogador_id)
VALUES (?, ?, ?, ?);
""", [
    ("Arthos", "Guerreiro", 15, 1),
    ("Lyra", "Mago", 22, 2),
    ("Talon", "Arqueiro", 10, 1)
])

cursor.executemany("""
INSERT INTO Itens (nome, tipo, valor)
VALUES (?, ?, ?);
""", [
    ("Espada Longa", "Arma", 120),
    ("Arco Élfico", "Arma", 150),
    ("Poção de Cura", "Poção", 50),
    ("Armadura de Ferro", "Armadura", 200),
    ("Anel Místico", "Acessório", 500)
])


cursor.executemany("""
INSERT INTO Inventario (personagem_id, item_id, quantidade)
VALUES (?, ?, ?);
""", [
    (1, 1, 1),  # Arthos tem 1 Espada Longa
    (1, 4, 1),  # Arthos tem 1 Armadura
    (2, 5, 1),  # Lyra tem 1 Anel Místico
    (2, 3, 5),  # Lyra tem 5 Poções de Cura
    (3, 2, 1)   # Talon tem 1 Arco Élfico
])

conn.commit()



def listar_jogadores():
    print("\n🎮 Lista de todos os jogadores:")
    cursor.execute("SELECT id, nickname, email, data_criacao FROM Jogadores;")
    for row in cursor.fetchall():
        print(row)

def jogadores_com_magos():
    print("\n🧙 Jogadores com personagens da classe 'Mago':")
    cursor.execute("""
    SELECT DISTINCT j.nickname
    FROM Jogadores j
    JOIN Personagens p ON j.id = p.jogador_id
    WHERE p.classe = 'Mago';
    """)
    for row in cursor.fetchall():
        print(row[0])

def item_mais_valioso():
    print("\n💎 Item mais valioso do jogo:")
    cursor.execute("SELECT nome, valor FROM Itens ORDER BY valor DESC LIMIT 1;")
    item = cursor.fetchone()
    print(f"{item[0]} (valor: {item[1]})")



listar_jogadores()
jogadores_com_magos()
item_mais_valioso()

conn.close()
print("\n✅ Banco de dados criado e consultas executadas com sucesso!")
