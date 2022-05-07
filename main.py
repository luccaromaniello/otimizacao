from classes.associacaoRequisitoValor import associacaoRequisitoValor
from classes.requisito import Requisito
from classes.stakeholder import Stakeholder
from knapsack import runKnapsack

requisito1 = Requisito(1, 'feature cadastro', 2)
requisito2 = Requisito(2, 'feature login', 3)
requisito3 = Requisito(3, 'feature salvar cartao', 5)
requisito4 = Requisito(4, 'feature buscar produtos', 8)
requisito5 = Requisito(5, 'feature finalizar compra', 12)

# juninho é um stakeholder que deseja priorizar as features iniciais
stakeholder1 = Stakeholder('juninho', [associacaoRequisitoValor(requisito1.id, 5),
                                        associacaoRequisitoValor(requisito2.id, 4), 
                                        associacaoRequisitoValor(requisito3.id, 2), 
                                        associacaoRequisitoValor(requisito4.id, 3), 
                                        associacaoRequisitoValor(requisito5.id, 1)])

# beatriz é uma stakeholder que quer vender os produtos mesmo sem cadastro
stakeholder2 = Stakeholder('beatriz', [associacaoRequisitoValor(requisito1.id, 1), 
                                        associacaoRequisitoValor(requisito2.id, 2), 
                                        associacaoRequisitoValor(requisito3.id, 3),
                                        associacaoRequisitoValor(requisito4.id, 4),
                                        associacaoRequisitoValor(requisito5.id, 5)])

# bolt é um stakeholder que quer priorizar a retenção de usuários
stakeholder3 = Stakeholder('bolt', [associacaoRequisitoValor(requisito1.id, 5),
                                        associacaoRequisitoValor(requisito2.id, 4),
                                        associacaoRequisitoValor(requisito3.id, 3),
                                        associacaoRequisitoValor(requisito4.id, 1),
                                        associacaoRequisitoValor(requisito5.id, 2)])

requisitos = [requisito1, requisito2, requisito3, requisito4, requisito5]
stakeholders = [stakeholder1, stakeholder2, stakeholder3]
numeroRequisitosRelease = 2

# rodar o knapsack, onde o valor é o valor do requisito pro stakeholder, peso é o esforço do requisito p ser implementado e o limite é numeroRequisitosRelease
def obterMelhorRelease(stakeholder):
    valoresRequisitos = []
    esforcosRequisitos = []
    for vr in stakeholder.requisitos:
        valoresRequisitos.append(vr.valorRequisito)
    for r in requisitos:
        esforcosRequisitos.append(r.esforco)
    return runKnapsack(numeroRequisitosRelease, esforcosRequisitos, valoresRequisitos, 0, requisitos, [])

# rodar o knapsack, onde o valor é a satisfação total de cada release, peso é o esforço total da release e o limite é o numeroRequisitosRelease
def obterMelhorReleasePossivel(release1, release2, release3):
    return

melhorReleaseJuninho = obterMelhorRelease(stakeholder1)
melhorReleaseBia = obterMelhorRelease(stakeholder2)
melhorReleaseBolt =  obterMelhorRelease(stakeholder3)
print(melhorReleaseJuninho)
print(melhorReleaseBia)
print(melhorReleaseBolt)

# melhorReleasePossivel = obterMelhorReleasePossivel(melhorReleaseJuninho, melhorReleaseBia, melhorReleaseBolt)
