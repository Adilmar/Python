# Function definition is here

def funcao1():                               #basic function
   print "Essa e uma funcao"                 #print basic text
   
def soma(x,y):                               #function sun (x,y) parameters
    soma = x+y;                              #calculate
    print "A soma e ",soma                   #return sun x+y
    
def verifica(x):                             #function pair / odd
    resto = x%2;                             #calculate mod division by 2
    if(resto == 0):
        print "Numero par"
    else:
        print "Numero impar"
    
funcao1()    # call the function
soma(2,5)
verifica(5)

