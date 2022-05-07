class Requisito:
    def __init__(self, id, descricao, esforco):
        self.id = id
        self.descricao = descricao
        self.esforco = esforco

    def __str__(self):
     return "id: " + str(self.id) + " - descricao: " + self.descricao + " - esforço: " + str(self.esforco)