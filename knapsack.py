# A naive recursive implementation
# of 0-1 knapsack Problem
 
# Returns the maximum valorRequisitoue that
# can be put in a knapsack of
# capacity limiteRequisitosRelease
 
def knapsack(limiteRequisitosRelease, esforco, valorRequisito, n, numRequisitosSelecionados, requisitos, requisitosFinais):
 
    # Base Case
    if n == 0 or limiteRequisitosRelease == 0 or numRequisitosSelecionados > limiteRequisitosRelease:
        return 0
 
    # If esforco of the nth item is
    # more than knapsack of capacity limiteRequisitosRelease,
    # then this item cannot be included
    # in the optimal solution

    if (esforco[n-1] < limiteRequisitosRelease):
        return knapsack(limiteRequisitosRelease, esforco, valorRequisito, n-1, numRequisitosSelecionados, requisitos, requisitosFinais), 
 
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
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
        
        # return max(
        #     valorRequisito[n-1] + knapsack(
        #         limiteRequisitosRelease-esforco[n-1], esforco, valorRequisito, n-1, numRequisitosSelecionados),
        #     knapsack(limiteRequisitosRelease, esforco, valorRequisito, n-1, numRequisitosSelecionados))
 
# end of function knapsack

def runKnapsack(limiteRequisitosRelease, esforco, valorRequisito, numRequisitosSelecionados, requisitos, requisitosFinais):
    return knapsack(limiteRequisitosRelease, esforco, valorRequisito, len(valorRequisito), numRequisitosSelecionados, requisitos, requisitosFinais)
