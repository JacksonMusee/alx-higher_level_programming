#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is not None and len(a_dictionary) > 0:
        values = a_dictionary.values()
        max_val = max(values)

        for k, v in a_dictionary.items():
            if v == max_val:
                max_key = k
        return max_key
