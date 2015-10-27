#!/usr/bin/python2

from __future__ import print_function


class StatBlock:

    def __init__(self, *args, **kwargs):
        self.attributes = kwargs

    def get_stat(self, stat):
        try:
            return self.attributes[stat](self)
        except TypeError, KeyError:
            pass
        try:
            return self.attributes[stat]
        except KeyError:
            return None

    def __getitem__(self, item):
        return self.get_stat(item)

    def __setitem__(self, key, value):
        self.attributes[key] = value

    def __iter__(self):
        return iter(self.attributes)

if __name__ == '__main__':
    sb = StatBlock(strength=15,
                   dexterity=15,
                   endurance=15,
                   intelligence=15,
                   wit=15,
                   presense=15,
                   luck=15,
                   health=lambda s: s['dexterity'] / 4 +
                                    s['strength'] / 2 +
                                    s['endurance'])

    for key in sb:
        print('{key}: {sb}'.format(key=key, sb=sb[key]))
