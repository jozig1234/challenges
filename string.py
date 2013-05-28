# -*- coding: iso-8859-1 -*-
'''
Created on 2013-05-28

@author: Emanuel
'''

#Étant donné une chaîne de charactère, eg: 'Daniel' ou 'Lucas', retourn une salutation de ce format: 'Bonjour Daniel!' ou 'Boujour Lucas!'
def bonjour(nom):
    #Votre code ici
    return #Votre réponse ici


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