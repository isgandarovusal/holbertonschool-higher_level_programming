#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best_k = None
    max_val = 0

    for k, v in a_dictionary.items():
        if best_k is None or v > max_val:
            max_val = v
            best_k = k
    return best_k
