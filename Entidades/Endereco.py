class Endereco():
    """docstring for Endereco."""
    def __init__(self, id_endereco, logradouro, complemento, bairro, cep, numero):
        super(Endereco, self).__init__()
        self.id_endereco = id_endereco
        self.logradouro = logradouro
        self.complemento = complemento
        self.bairro = bairro
        self.cep = cep
        self.numero = numero
