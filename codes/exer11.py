# coding: utf-8

lista = [ 'adilmar', 786 , 2.23, 'pedro', 70.2 ]

print("LISTA\n")

print lista          # Prints complete list
print lista[0]       # Prints first element of the list
print lista[1:3]     # Prints elements starting from 2nd till 3rd 
print lista[2:]      # Prints elements starting from 3rd element

print("\nTUPLA\n")

tupla = ( 'adilmar', 786 , 2.23, 'pedro', 70.2  )
tinytuple = (123, 'jose')

print tupla           # Prints complete list
print tupla[0]        # Prints first element of the list
print tupla[1:3]      # Prints elements starting from 2nd till 3rd 
print tupla[2:]       # Prints elements starting from 3rd element
print tinytuple * 2   # Prints list two times
print tupla + tinytuple # Prints concatenated lists
print("\nDicionário\n")

tinydict = {'nome': 'adilmar','codigo':6734, 'departamento': 'TI'}
print tinydict          # Prints complete dictionary
print tinydict.keys()   # Prints all the keys
print tinydict.values() # Prints all the values
