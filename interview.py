'''
Created on 2013-05-18

@author: Emanuel

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
heres both int and str challenges completed.
int
def exposant(n):
      return n**2

#Étant donné un nombre, retourne ce nombre modulo deux. Que remarque tu?
def modulo(n):
    return n%2

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
    
str

def bonjour(nom):
    n = "Bonjour " + nom + "!"
    return n


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
