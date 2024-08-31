import mysql.connector

# Estabelecer a conexão
conexao = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="controle_gastos_pessoais"
)

# Criar um cursor
cursor = conexao.cursor()

# Executar uma consulta
cursor.execute("SELECT nome, sobrenome FROM usuarios")

# Buscar os resultados
for (nome, sobrenome) in cursor:
    print(f"Nome: {nome} {sobrenome}")

# Fechar o cursor e a conexão
cursor.close()
conexao.close()