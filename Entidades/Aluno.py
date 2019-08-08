class Aluno():
    """docstring for Aluno."""
    def __init__(self, id_aluno, nome, matricula, cpf, nascimento):
        super(Aluno, self).__init__()
        self.id_aluno = id_aluno
        self.nome = nome
        self.matricula = matricula
        self.cpf = cpf
        self.nascimento = nascimento
