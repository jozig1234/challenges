# -*- coding: iso-8859-1 -*-
'''
Created on 2013-05-28

@author: Emanuel
'''

#�tant donn� une cha�ne de charact�re, eg: 'Daniel' ou 'Lucas', retourne une salutation dans le format suivant: 'Bonjour Daniel!' ou 'Boujour Lucas!'
def bonjour(nom):
    #Votre code ici
    return #Votre r�ponse ici


#Ignorez le restant
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))
    
def main():
    test(bonjour('Scout'), 'Bonjour Scout!')
    test(bonjour('Jem'), 'Bonjour Jem!')
    test(bonjour('Dill'), 'Bonjour Dill!')
    test(bonjour('Atticus'), 'Bonjour Atticus!')

if __name__ == '__main__':
    main()