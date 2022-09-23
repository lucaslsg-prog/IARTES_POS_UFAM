import pytest
import validation

class TestEmail(object):

    def test_email_sem_arroba(self):
        email = 'username.gmail.com'
        assert validation.check_email(email) == False

    def test_email_com_espaco(self):
        email = 'username @gmail.com'
        assert validation.check_email(email) == False
    
    def test_email_sem_ponto_com(self):
        email = 'username@gmail'
        assert validation.check_email(email) == False

    def test_email_valido(self):
            email = 'username@gmail.com'
            assert validation.check_email(email) == True
