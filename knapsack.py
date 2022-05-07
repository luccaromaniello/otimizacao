# Implementação do knapsack
# idealmente, retorna a melhor release possível dos stakeholders
# nesse caso, retorna o valor máximo dos requisitos selecionados
 
def knapsack(limiteRequisitosRelease, esforco, valorRequisito, n, numRequisitosSelecionados, requisitos, requisitosFinais):
 
    # Base Case
    if n == 0 or limiteRequisitosRelease == 0 or numRequisitosSelecionados > limiteRequisitosRelease:
        return 0
 
    # se o esforco do item n for maior que a capacidade da mochila (nesse caso, o limite de requisitos da release, o item não é incluso na solução ótima

    if (esforco[n-1] < limiteRequisitosRelease):
        return knapsack(limiteRequisitosRelease, esforco, valorRequisito, n-1, numRequisitosSelecionados, requisitos, requisitosFinais), 
 
    retorna o máximo de dois casos: o n-ésimo item incluso ou não é incluso / adiciona na lista de requisitos finais
    else:
        v2 = knapsack(limiteRequisitosRelease, esforco, valorRequisito, n-1, numRequisitosSelecionados, requisitos, requisitosFinais)
        v = valorRequisito[n-1] + knapsack(limiteRequisitosRelease-esforco[n-1], esforco, valorRequisito, n-1, numRequisitosSelecionados, requisitos, requisitosFinais)
        if v > v2:
            numRequisitosSelecionados = numRequisitosSelecionados + 1
            for r in requisitos:
                for e in esforco:
                    if r.esforco == e:
                        requisitosFinais.append(r.descricao)

        print(requisitosFinais)
        return max(v, v2)
        
        # função original, sem a verificação dos requisitos
        
        # return max(
        #     valorRequisito[n-1] + knapsack(
        #         limiteRequisitosRelease-esforco[n-1], esforco, valorRequisito, n-1, numRequisitosSelecionados),
        #     knapsack(limiteRequisitosRelease, esforco, valorRequisito, n-1, numRequisitosSelecionados))
 
def runKnapsack(limiteRequisitosRelease, esforco, valorRequisito, numRequisitosSelecionados, requisitos, requisitosFinais):
    return knapsack(limiteRequisitosRelease, esforco, valorRequisito, len(valorRequisito), numRequisitosSelecionados, requisitos, requisitosFinais)
