# algoritmo para validar email e cpf

def check_email(email):
    dominios_email = ('gmail','hotmail','yahoo','icloud','outlook')
    email_valido = True
    if '@' not in email:
        email_valido = False
        print("Email invalido, insira o '@'")

    elif email.islower() != True:
        email_valido = False
        print("Email invalido, insira apenas letras minusculas")

    elif '.com' not in email:
        email_valido = False
        print("Email invalido, insira '.com'")
    
    elif (email.split("@",1)[1]).split('.com')[0] not in dominios_email:
        email_valido = False
        print("Email invalido, inisira um domínio valido após '@'")

    elif ' ' in email:
        email_valido = False
        print("Email invalido, insira email sem espaço")

    else:
        email_valido = True
    
    return email_valido

import string

def check_cpf(cpf):
    cpf_valido = True
    minusculas = list(string.ascii_lowercase)
    maiusculas = list(string.ascii_uppercase)
    letras = minusculas+maiusculas
    for i in range(len(letras)):
        if letras[i] not in cpf:
            pass
        else:
            cpf_valido = False
            print("CPF invalido")

    if '.' in cpf:
        cpf_valido = False
        print("CPF invalido")

    elif '-' in cpf:
        cpf_valido = False
        print("CPF invalido")

    if len(cpf) == 14:
        
        primeiraParte = cpf.split('.')[0]
        segundaParte = cpf.split('.')[1]
        terceiraParte = (cpf.split('.')[2]).split('-')[0]
        quartaParte = (cpf.split('.')[2]).split('-')[1]
        digitos_string = primeiraParte + segundaParte + terceiraParte + quartaParte
        
        list_soma1 = []
        list_soma2 = []
        if len(digitos_string) == 11 and digitos_string.isdigit():

            multiplicador=10
            for digito in range(0,9):
                list_soma1.append(multiplicador*int(digitos_string[digito]))
                multiplicador-=1

            if (sum(list_soma1)*10)%11 == int((cpf.split('.')[2]).split('-')[1][0]):

                multiplicador=11  
                for digito in range(0,10):
                    list_soma2.append(multiplicador*int(digitos_string[digito]))
                    multiplicador-=1

                if (sum(list_soma2)*10)%11 == int((cpf.split('.')[2]).split('-')[1][1]):
                    cpf_valido = True
                    
                else:
                    cpf_valido = False
                    print("CPF invalido")
            else:
                cpf_valido = False
                print("CPF invalido")

        else:
            cpf_valido = False
            print("CPF invalido")

    else:
        cpf_valido = False
        print("CPF invalido")


    return cpf_valido