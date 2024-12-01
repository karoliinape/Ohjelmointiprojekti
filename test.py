import unittest
import os
from Salasanaohjelma import is_strong_password, add_password, get_password, save_passwords, load_passwords, websites, usernames, encrypted_passwords

class TestPasswordManager(unittest.TestCase):

# tekee testi filen nimeltä test_vault.txt ennen jokaista testiä
    def setUp(self):
        self.test_file = "test_vault.txt"
        websites.clear()
        usernames.clear()
        encrypted_passwords.clear()

   # poistaa testi filen, jokaisen testin jälkeen    
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        websites.clear()
        usernames.clear()
        encrypted_passwords.clear()

# testaa fukntion is_strong_password eri salasanoilla
    def test_is_strong_password(self):
        self.assertTrue(is_strong_password("ValidPassword1"))
        self.assertFalse(is_strong_password("short1"))
        self.assertFalse(is_strong_password("nouppercase1"))
        self.assertFalse(is_strong_password("NOLOWERCASE1"))
        self.assertFalse(is_strong_password("NoDigits"))

#testaa addpassword funktion
    def test_add_password(self):
        self.assertTrue(add_password("newsite.com", "newuser", "NewPassword1"))
        self.assertFalse(add_password("newsite.com", "newuser", "weakpassword"))

#testaa funktion get_password
    def test_get_password(self):
        add_password("example.com", "user1", "Password123")
        username, password = get_password("example.com")
        self.assertEqual(username, "user1")
        self.assertEqual(password, "Password123")

# testaa funktion save_password
    def test_save_passwords(self):
        add_password("example.com", "user1", "Password123")
        save_passwords(self.test_file)
        self.assertTrue(os.path.exists(self.test_file))

# testaa funktion test_load_passwords
    def test_load_passwords(self):
        add_password("example.com", "user1", "Password123")
        save_passwords(self.test_file)
        data = load_passwords(self.test_file)
        self.assertEqual(data["websites"], ["example.com"])
        self.assertEqual(data["usernames"], ["user1"])
        self.assertEqual(data["encrypted_passwords"], encrypted_passwords)

if __name__ == '__main__':
    unittest.main()
