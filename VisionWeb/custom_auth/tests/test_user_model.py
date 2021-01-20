from django.test import TestCase

from custom_auth.tests.common import create_user
from custom_auth.tests.common import create_superuser


class CreateAuthUser(TestCase):
    """Unit testing unthentication user model"""

    def test_create_user_valid_data(self):
        """Test pure user model with valid data"""
        payload = {
            'username': 'testusername',
            'email': 'foo@bar.com',
            'password': 'foobar123'
        }

        user = create_user(**payload)

        self.assertEqual(user.username, 'testusername')
        self.assertEqual(user.email, 'foo@bar.com')
        self.assertTrue(user.check_password('foobar123'))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_user_invalid_data(self):
        """Test pure user model with invalid data"""
        with self.assertRaises(TypeError):
            create_user()
        with self.assertRaises(ValueError):
            create_user(username='', email='')
        with self.assertRaises(ValueError):
            create_user(username='', email='', password='foo')

    def test_create_superuser_valid_data(self):
        """Test superuser model with valid data"""
        payload = {
            'username': 'testsudoname',
            'email': 'sudo@bar.com',
            'password': 'testsudopass'
        }

        sudo = create_superuser(**payload)

        self.assertEqual(sudo.username, 'testsudoname')
        self.assertEqual(sudo.email, 'sudo@bar.com')
        self.assertTrue(sudo.check_password('testsudopass'))
        self.assertTrue(sudo.is_active)
        self.assertTrue(sudo.is_staff)
        self.assertTrue(sudo.is_superuser)

    def test_create_superuser_invalid_data(self):
        """Test superuser model with is_superuser: 'False'"""
        with self.assertRaises(ValueError):
            create_superuser(
                username='example',
                email='super@user.com',
                password='foo',
                is_superuser=False
            )

    def test_force_login(self):
        payload = {
            'username': 'testusername',
            'email': 'foo@bar.com',
            'password': 'foobar123'
        }

        user = create_user(**payload)
        user.set_password(payload['password'])
        self.assertTrue(self.client.login(
            username='testusername',
            password='foobar123'
        ))
