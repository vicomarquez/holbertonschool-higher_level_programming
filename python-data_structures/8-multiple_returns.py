#!/usr/bin/python3i
def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    return len(sentence), sentence[0]
