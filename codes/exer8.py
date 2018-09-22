#!/usr/bin/python
# -*- coding: utf8 -*-

fp = open('dados.txt') # abre o arquivo 
lines = fp.read().split("\n") # cria uma lista
print(lines)
fp.close() # close file

print "\nFazendo de outra maneira\n"

with open('dados.txt') as fp:
    for line in fp:
        print line
