import myform
import unittest
import re

list_mail_cor = ["m.m@mail.ru",
                 "m1@gmail.com",
                 "hyt@mail.com",
                 "rwfrge@mail.com",
                 "aa@mail.ru"]

list_mail_uncor = ["",
                   "1",
                   "m1@",
                   "@mail",
                   "user@mail.com!",
                   "usermail.com",
                   "user@@mail.com",
                   "user @ mail.com",
                   "user@mail!.com",
                   "@.com",
                   "user@"]

class MailTest(unittest.TestCase):
    def test_T_mail(self):
        for mail in list_mail_cor:
            self.assertTrue(re.fullmatch(myform.REGEX, mail))
    
    def test_F_mail(self):
        for mail in list_mail_uncor:
            self.assertFalse(re.fullmatch(myform.REGEX, mail))
        
if __name__ == '__main__':
    unittest.main()