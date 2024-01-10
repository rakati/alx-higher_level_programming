#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    mx = None
    res = None
    for k, v in a_dictionary.items():
        if mx is None or v > mx:
            res = k
            mx = v
    return res
