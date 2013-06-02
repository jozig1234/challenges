'''
Created on 2013-05-18

@author: Emanuel
test
Create a program that asks the user for his
name and his age. With that information,
calculate his year of birth.

Output the information to the console
in this format:
Your name is (blank) and you are (blank) years old.
You were born in (blank).

If he is one year old, write 'and you are 1 year old!'.
If he us zero years old, write 'and you are still a baby!'
If he enters a negative number, write 'and I don't speak to time travellers!'. Don't tell
him what year he was born in either.

--------------------
What is your name?: manny
How old are you:? 16
Your name is manny and you are 16 years old.
You were born in 1997.
--------------------
'''
string challenge: help with this one

#Étant donné une chaîne de charactère, eg: 'Daniel' ou 'Lucas', retourn une salutation de ce format: 'Bonjour Daniel!' ou 'Boujour Lucas!'
def bonjour(N):
    Nom = "Bonjour" + N + "!"
    return Nom 


#http://repl.it/languages/PythonIgnorez le restant
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
