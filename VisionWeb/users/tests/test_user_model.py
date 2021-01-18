from django.test import TestCase

from users.tests.common import create_user
from users.tests.common import create_superuser


class CreateAuthUser(TestCase):
    """Unit testing unthentication user model"""

    def test_create_user_valid_data(self):
        """Test pure user model with valid data"""
        payload = {
            'email': 'foo@bar.com',
            'password': 'foobar123'
        }

        user = create_user(**payload)

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
            create_user(email='')
        with self.assertRaises(ValueError):
            create_user(email='', password='foo')

    def test_create_superuser_valid_data(self):
        """Test superuser model with valid data"""
        payload = {
            'email': 'sudo@bar.com',
            'password': 'testsudopass'
        }

        sudo = create_superuser(**payload)

        self.assertEqual(sudo.email, 'sudo@bar.com')
        self.assertTrue(sudo.check_password('testsudopass'))
        self.assertTrue(sudo.is_active)
        self.assertTrue(sudo.is_staff)
        self.assertTrue(sudo.is_superuser)

    def test_create_superuser_invalid_data(self):
        """Test superuser model with is_superuser: 'False'"""
        with self.assertRaises(ValueError):
            create_superuser(
                email='super@user.com',
                password='foo',
                is_superuser=False
            )

    def test_force_login(self):
        payload = {
            'email': 'foo@bar.com',
            'password': 'foobar123'
        }

        user = create_user(**payload)
        user.set_password(payload['password'])
        self.assertTrue(self.client.login(
            email='foo@bar.com',
            password='foobar123'
        ))
