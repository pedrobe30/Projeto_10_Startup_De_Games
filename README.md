# Projeto 11: Jogo "PixelVerse Adventures" ⚔️🛡️
---
## O Cenário 👨‍💼

Você foi contratado(a) como o novo Administrador de Banco de Dados (DBA) júnior na "PixelVerse Studios", uma empresa que está desenvolvendo um novo RPG online de sucesso.

Atualmente, os game designers controlam todos os jogadores, personagens e itens do jogo em planilhas do Excel. É um caos! Quando um jogador ganha um item novo, um designer precisa editar a planilha do jogador E a planilha de itens para subtrair o estoque. É lento, propenso a erros e simplesmente não funciona para um jogo com milhares de jogadores.

Sua primeira e mais importante missão é projetar e construir a espinha dorsal do jogo: um banco de dados relacional robusto usando **SQLite** para gerenciar de forma eficiente e segura todos os jogadores, seus personagens e seus inventários.

### 💡 O que é um Banco de Dados Relacional?
Pense em um banco de dados como um arquivo de fichas super organizado. Cada "gaveta" é uma **tabela** (ex: `Jogadores`, `Itens`). Dentro de cada gaveta, as "fichas" são as **linhas** (cada jogador ou item específico) e cada informação na ficha é uma **coluna** (ex: `nome`, `email`, `dano`). A "mágica" acontece quando usamos **chaves** (`PRIMARY KEY` e `FOREIGN KEY`) para criar "fios" que conectam as fichas de diferentes gavetas, criando relacionamentos lógicos entre elas.

## 📋 Requisitos da Missão

A equipe de desenvolvimento precisa de uma base sólida para construir o jogo. Seu banco de dados deve atender aos seguintes requisitos:

1.  **Criar o Banco de Dados:** O script deve criar um único arquivo de banco de dados chamado `game_database.db`.

2.  **Modelar as Tabelas:** Você precisa projetar e criar 4 tabelas principais para representar a lógica do jogo:
    * **`Jogadores`**: Para armazenar as contas dos usuários.
        * `id` (Chave Primária, Inteiro)
        * `nickname` (Texto, Único)
        * `email` (Texto, Único)
        * `data_criacao` (Data/Texto)
    * **`Personagens`**: Um jogador pode ter vários personagens.
        * `id` (Chave Primária, Inteiro)
        * `nome` (Texto)
        * `classe` (Texto, ex: 'Guerreiro', 'Mago', 'Arqueiro')
        * `nivel` (Inteiro)
        * `jogador_id` (**Chave Estrangeira** que se conecta com a tabela `Jogadores`)
    * **`Itens`**: O catálogo de todos os itens que existem no jogo.
        * `id` (Chave Primária, Inteiro)
        * `nome` (Texto, Único)
        * `tipo` (Texto, ex: 'Arma', 'Armadura', 'Poção')
        * `valor` (Inteiro)
    * **`Inventario`**: A tabela que conecta quais personagens possuem quais itens (relação Muitos-para-Muitos).
        * `id` (Chave Primária, Inteiro)
        * `personagem_id` (**Chave Estrangeira** que se conecta com `Personagens`)
        * `item_id` (**Chave Estrangeira** que se conecta com `Itens`)
        * `quantidade` (Inteiro)

3.  **Popular com Dados:** Seu script deve inserir alguns dados de exemplo (`INSERT INTO`) para que seja possível testar as consultas. Crie pelo menos 2 jogadores, 3 personagens e 5 itens distintos. Distribua alguns itens nos inventários dos personagens.

4.  **Escrever Consultas (`Queries`):** O objetivo final! Seu script deve ser capaz de responder a perguntas complexas dos game designers, por exemplo:
    * "Lista de todos os jogadores cadastrados"
    * "Quais jogadores possuem personagens da classe 'Mago'?"
    * "Qual é o item mais valioso do jogo?"
    * Easter egg: você que prestou atenção no readme, vale um pirulito.

## 💡 Roteiro Sugerido para o Sucesso

1.  **Importe** a biblioteca `sqlite3`.
2.  **Conecte-se** ao banco de dados (o arquivo será criado se não existir).
3.  **Crie as 4 tabelas** usando `CREATE TABLE`. Preste muita atenção na sintaxe de `PRIMARY KEY AUTOINCREMENT`, `FOREIGN KEY` e `REFERENCES`.
4.  **Insira os dados de exemplo** com o comando `INSERT INTO`. Lembre-se de usar `conn.commit()` para salvar as alterações.
5.  **Escreva as funções de consulta**: Crie uma função Python para cada pergunta de negócio. Dentro delas, escreva o comando `SELECT`.
7.  **Busque e imprima os resultados** usando `cursor.fetchall()` e um loop `for` para exibir os dados de forma legível.
8.  **Feche a conexão** no final do script com `conn.close()`.