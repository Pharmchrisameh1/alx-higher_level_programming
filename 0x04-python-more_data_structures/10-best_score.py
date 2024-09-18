#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    bestKey = list(a_dictionary)[0]
    bestValue = a_dictionary[bestKey]

    for k, v in a_dictionary.items():
        if v > bestValue:
            bestValue = v
            bestKey = k
    return bestKey
