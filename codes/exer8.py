fp = open('C://dados.txt') # abre o arquivo 
lines = fp.read().split("\n") # cria uma lista
print(lines)
fp.close() # close file

print "\nFazendo de outra maneira\n"

with open('C://dados.txt') as fp:
    for line in fp:
        print line
