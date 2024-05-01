# Importando SQLite
import sqlite3 as lite

# Criando conexão 
con = lite.connect('dados.db')

# Tabela de Categoria 
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Categoria(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")

# Tabela de Receitas
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE receitas(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, adicionando_em DATE, valor DEDIMAL)")

# Tabela de Gastos 
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Gastos(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, valor DECIMAL)")

