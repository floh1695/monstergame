#!/usr/bin/python2

from __future__ import print_function

class StatBlock:
    """

    """
    def __init__(self, *args, **kwargs):
        self.attributes = kwargs

    def get_stat(self, stat):
        try:
            return self.attributes[stat](self)
        except:
            pass
        try:
            return self.attributes[stat]
        except:
            return None


if __name__ == '__main__':
    sb = StatBlock(strength=15,
                   dexterity=15,
                   endurance=15,
                   intelligence=15,
                   wit=15,
                   presense=15,
                   luck=15,
                   health=lambda s: s.get_stat('dexterity') / 4 +
                                    s.get_stat('strength') / 2 +
                                    s.get_stat('endurance'))
    for key in sb.attributes:
        print('{key}: {sb}'.format(key=key, sb=sb.get_stat(key)))
