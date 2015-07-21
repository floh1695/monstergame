#!/usr/bin/python2

from random import gauss
    
_name_change = 100 

def _random_personality():
    return gauss(0, _name_change * 1.5)

def _score_name_picker(score, names):
    if score >= _name_change:
        return names[0]
    elif score <= -_name_change:
        return names[2]
    else:
        return names[1]

class PersonalitySegment:
    def __init__(self):
        pass

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

    def score_n_data(self):
        return _score_name_picker(self.score_n,
                ('Reactive', 'Responsive', 'Resilient'))

    def score_e_data(self):
        return _score_name_picker(self.score_c,
                ('Extravert', 'Ambivert', 'Introvert'))

    def score_o_data(self):
        return _score_name_picker(self.score_o,
                ('Explorer', 'Moderate', 'Preserver'))

    def score_a_data(self):
        return _score_name_picker(self.score_a,
                ('Adapter', 'Negotiator', 'Challenger'))

    def score_c_data(self):
        return _score_name_picker(self.score_c,
                ('Focused', 'Balanced', 'Flexible'))

    def __str__(self):
        return str((
                self.score_n_data(),
                self.score_e_data(),
                self.score_o_data(),
                self.score_a_data(),
                self.score_c_data()))

if __name__ == '__main__':
    print('Unit test for ./personality.py')
    p1 = Personality()
    print(p1)

