# -*- coding: iso-8859-1 -*-
'''
Created on 2013-05-28

@author: Emanuel
'''

#Étant donné un nombre, retourne ce nombre à l'exposant deux.
def exposant(n):
    return

#Étant donné un nombre, retourne ce nombre modulo deux. Que remarque tu?
def modulo(n):
    return

#Ignorez le restant
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))
    
def main():
    print 'Exposant:'
    test(exposant(2), 4)
    test(exposant(8), 64)
    test(exposant(0), 0)
    test(exposant(15), 225)

    print 'Modulo:'
    test(modulo(5), 1)
    test(modulo(10), 0)
    test(modulo(27), 1)
    test(modulo(8), 0)


if __name__ == '__main__':
    main()