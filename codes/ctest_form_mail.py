import unittest

from PankovVasya021.my_form_mail import *


class FormTest(unittest.TestCase):
    """Тесты на правильность проверки электронной почты"""

    # Список с неправильными значениями почты
    list_mail_uncor = ["", "a@", "pa", "pank@a", "@a", "pank@pank", "       @   . ", "pank@pank.", "pank@pank,su",
                       "pank@pank.su, pank@pank.su", "        ", "vasya.pankov@ma", "pa@pa@.com", "misha....palok"]
    # Список с привильными значениями почты
    list_mail_cor = ["pank@pank.su", "vasya.pankov26@gamil.com", "vasya_@mail.com",
                     "veryveryveryveryveryveryveryveryveryveryveryveryvery@longlonglonglong.email", "&=_‘-+@sym.love",
                     "SENSETIVE@UPPER.CASE"]

    def test_F_mail(self):
        """Проверка некорректных адресов"""
        for mail in self.list_mail_uncor:
            self.assertFalse(mail_is_correct(mail))

    def test_T_mail(self):
        """Проверка корректных адресов"""
        for mail in self.list_mail_cor:
            self.assertTrue(mail_is_correct(mail))
