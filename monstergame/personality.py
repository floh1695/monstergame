#!/usr/bin/python2

from random import gauss
    
_name_change = 100 

def _random_personality():
    return gauss(0, _name_change * 1.5)

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

    def score_n_name(self):
        name = ''
        if self.score_n >= _name_change:
            name = 'high N'
        elif self.score_n <= -_name_change:
            name = 'low N'
        else:
            name = 'modest N'
        return name

    def score_e_name(self):
        name = ''
        if self.score_e >= _name_change:
            name = 'high E'
        elif self.score_e <= -_name_change:
            name = 'low E'
        else:
            name = 'modest E'
        return name

    def score_o_name(self):
        name = ''
        if self.score_o >= _name_change:
            name = 'high O'
        elif self.score_o <= -_name_change:
            name = 'low O'
        else:
            name = 'modest O'
        return name

    def score_a_name(self):
        name = ''
        if self.score_a >= _name_change:
            name = 'high A'
        elif self.score_a <= -_name_change:
            name = 'low A'
        else:
            name = 'modest A'
        return name

    def score_c_name(self):
        name = ''
        if self.score_c >= _name_change:
            name = 'high C'
        elif self.score_c <= -_name_change:
            name = 'low C'
        else:
            name = 'modest C'
        return name

    def __str__(self):
        return str((
                self.score_n_name(),
                self.score_e_name(),
                self.score_o_name(),
                self.score_a_name(),
                self.score_c_name()))

if __name__ == '__main__':
    print('Unit test for ./personality.py')
    p1 = Personality()
    print(p1)

