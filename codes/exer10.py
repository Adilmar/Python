# -*- coding: cp1252 -*-
op='0'


print (":::::::::::::::::::::Agenda Eletronica:::::::::::::::::::::")
print ("\nLISTA DE OPÇÕES\n1-Inserir\n2-Listar")


while(op=='0'):
    opcao = raw_input("\nDigite uma opção: ")

    if(opcao=='1'):
        file = open("agenda.txt","a")
        op='1'
        print("\nOPÇÃO SELECIONADA: INSERIR CONTATO")
        nome = raw_input("\nInforme o nome: ")
        celular = raw_input("Informe o celular: ")
        fixo = raw_input("Informe o Fixo: ")
        email = raw_input("Informe o email: ")
        ano = raw_input("Informe o ano de nascimento: ")
        idade= 2017 - int(ano);

        file.write("Nome: "     +nome        +"\n")
        file.write("Celular: "  +celular     +"\n")
        file.write("Fixo: "     +fixo        +"\n")
        file.write("email: "    +email       +"\n")
        file.write("Idade: "    +str(idade)  +"\n")
        file.write("-------------------------------\n")
        file.close()
        op='0'

    if(opcao=='2'):
        file = open("agenda.txt","a")
        op='1'
        print("\nOPÇÃO SELECIONADA: LISTAR CONTATOS")
        with open("agenda.txt") as agenda:
            for contato in agenda:
                print contato
        file.close()
        

