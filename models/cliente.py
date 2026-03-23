class Cliente:
    def __init__(self, nome: str, cpf: str, telefone: str, email: str):
        self.nome = nome 
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
    
    def to_dict(self):
        return {
            "nome": self.nome,
            "cpf": self.cpf,
            "telefone": self.telefone,
            "email": self.email
        }
