from models.user import UserModel
import unittest


class AppTest(unittest.TestCase):
    def test_create_user(self):
        user = UserModel('test', 'abcd')

        self.assertEqual(user.username, 'test',)
        self.assertEqual(user.password, 'abcd',)
