import sqlite3

conn = sqlite3.connect('EscolaApp_versao2.db')

cursor = conn.cursor()


cursor.execute("""
    CREATE TABLE tb_escola(
        id_escola INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(45) NOT NULL,
        FK_id_endereco INTEGER NOT NULL,
        FK_id_campus INTEGER NOT NULL,
        FOREIGN KEY(fk_id_endereco) REFERENCES tb_endereco (idtb_endereco),
        FOREIGN KEY(fk_id_campus) REFERENCES tb_campus (id_campus)

    );
""")
print('Tabela tb_escola foi criada.')

cursor.execute("""
    CREATE TABLE tb_aluno(
        id_aluno INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(45) NOT NULL,
        matricula VARCHAR(12) NOT NULL,
        cpf VARCHAR(11) NOT NULL,
        nascimento DATE NOT NULL,
        FK_id_endereco INTEGER NOT NULL,
        FK_id_curso INTEGER NOT NULL,
        FOREIGN KEY(fk_id_endereco) REFERENCES tb_endereco (id_endereco),
        FOREIGN KEY(fk_id_curso) REFERENCES tb_curso (id_curso)
    );
""")

print('Tabela tb_aluno foi criada.')

cursor.execute("""
    CREATE TABLE tb_curso(
        id_curso INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(45) NOT NULL,
        FK_id_turno INTEGER NOT NULL,
        FOREIGN KEY(fk_id_turno) REFERENCES tb_turno (id_turno)
    );
""")

print('Tabela tb_curso foi criada.')


cursor.execute("""
    CREATE TABLE tb_turma(
        id_turma INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(45) NOT NULL,
        FK_id_curso INTEGER NOT NULL,
        FOREIGN KEY(fk_id_curso) REFERENCES tb_curso (id_curso)
    );
""")

print('Tabela tb_turma foi criada.')

cursor.execute("""
    CREATE TABLE tb_disciplina(
        id_disciplina INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(45) NOT NULL,
        FK_id_professor INTEGER NOT NULL,
        FOREIGN KEY(fk_id_professor) REFERENCES tb_professor (id_professor)
    );
""")

print('Tabela tb_disciplina foi criada.')

cursor.execute("""
    CREATE TABLE tb_endereco(
        id_endereco INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        logradouro VARCHAR(70)NOT NULL,
        complemento VARCHAR(45)NOT NULL,
        bairro VARCHAR(45)NOT NULL,
        cep VARCHAR(8)NOT NULL,
        numero INTEGER NOT NULL
    );
""")
print('Tabela tb_endereco foi criada.')

cursor.execute("""
    CREATE TABLE tb_campus(
        id_campus INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        sigla VARCHAR(3) NOT NULL,
        cidade VARCHAR(45) NOT NULL
    );
""")

print('Tabela tb_campus foi criada.')

cursor.execute("""
    CREATE TABLE tb_professor(
        id_professor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(45) NOT NULL,
        FK_id_endereco INT NOT NULL,
        FOREIGN KEY(fk_id_endereco) REFERENCES tb_endereco (id_endereco)

    );
""")

print('Tabela tb_professor foi criada.')

cursor.execute("""
    CREATE TABLE tb_turno(
        id_turno INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(10) NOT NULL

    );
""")

print('Tabela tb_turno foi criada.')


