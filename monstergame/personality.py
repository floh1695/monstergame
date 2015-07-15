#!/usr/bin/python2

from random import gauss
    
_name_change = 100 

def _random_personality():
    return gauss(0, _name_change)

class Personality(object):
    def __init__(self,
            score_n = _random_personality(),
            score_e = _random_personality(),
            score_o = _random_personality(),
            score_a = _random_personality(),
            score_c = _random_personality()):
        self.score_n = score_n # Need for Stability / Neuroticism
        self.score_e = score_e # Extravertion       / Sociability
        self.score_o = score_o # Originality        / Openness
        self.score_a = score_a # Accomidation       / Aggreableness
        self.score_c = score_c # Consolidation      / Conscientiousness

    def __str__(self):
        return str((self.score_n,
                self.score_e,
                self.score_o,
                self.score_a,
                self.score_c))

if __name__ == '__main__':
    print('Unit test for ./personality.py')
    p1 = Personality()
    print(p1)

