#!/usr/bin/env python


class Test(object):
    def __init__(self):
        self._text = []

    @property
    def text(self):
        print 'a'
        return self._text

    @text.setter
    def text(self, value):
        print 'b'
        print value
        self._text = value


t = Test()

print t.text

t.text.append({'asd':23})
print t.text