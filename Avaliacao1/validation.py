# algoritmo para validar email e cpf

# 1) casos de teste voltados para o que não deve ter em um email
# 2) casos de teste voltados para posições erradas ex: dominio@username


# email = input("Digite um email: ")
def check_email(email):
    email_valido = True
    if '@' not in email:
        email_valido = False
        print("Email invalido")

    elif ' ' in email:
        email_valido = False
        print("Email invalido")

    elif '.com' not in email:
        email_valido = False
        print("Email invalido")
    else:
        email_valido = True
    
    return email_valido
# check_email(email)