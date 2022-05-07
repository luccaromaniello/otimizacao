class associacaoRequisitoValor:
    def __init__(self, idRequisito, valorRequisito):
        self.idRequisito = idRequisito
        self.valorRequisito = valorRequisito

    def __str__(self):
        return "idRequisito: " + str(self.idRequisito) + " - valorRequisito: " + str(self.valorRequisito)