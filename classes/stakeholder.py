class Stakeholder:
    # requisitos é do tipo associacaoRequisitoValor
    def __init__(self, nome, requisitos):
        self.nome = nome
        self.requisitos = requisitos

    def __str__(self):
        return "nome: " + self.nome + " - requisitos: " + str(self.requisitos)