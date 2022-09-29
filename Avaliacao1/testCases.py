import pytest
import validation

class TestEmail(object):
    
    def test_email_sem_arroba(self):
        email = 'usernamegmail.com'
        assert validation.check_email(email) == False

    def test_email_com_letra_maiuscula(self):
        email = 'USERNAME@gmail.com'
        assert validation.check_email(email) == False

    def test_email_sem_ponto_com(self):
        email = 'username@gmail'
        assert validation.check_email(email) == False

    def test_email_sem_dominio_valido_apos_arroba(self):
        email = 'username@qualquercoisa.com'
        assert validation.check_email(email) == False

    def test_email_com_espaco(self):
        email = 'username @gmail.com'
        assert validation.check_email(email) == False
    
    def test_email_valido(self):
        email = 'username@gmail.com'
        assert validation.check_email(email) == True



class TestCPF(object):
    
    def test_cpf_com_letras(self):
        cpf = 'A27.0b5.4W2-2c'
        assert validation.check_cpf(cpf) == False
    
    def test_cpf_sem_ponto(self):
        cpf = '529982247-25'
        assert validation.check_cpf(cpf) == False

    def test_cpf_sem_hifen(self):
        cpf = '529.982.24725'
        assert validation.check_cpf(cpf) == False
    
    def test_cpf_mais_digitos_numericos(self):
        cpf = '5291982124712516567687889'
        assert validation.check_cpf(cpf) == False

    def test_cpf_primeiro_digito(self):
        cpf = '529.982.247-95'
        assert validation.check_cpf(cpf) == False
    
    def test_cpf_segundo_digito(self):
        cpf = '529.982.247-29'
        assert validation.check_cpf(cpf) == False

    def test_cpf_valido(self):
        cpf = '529.982.247-25'
        assert validation.check_cpf(cpf) == True