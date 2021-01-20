from __future__ import annotations

from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase
from rest_framework.response import Response
from rest_framework import status

from custom_auth.tests.common import create_user

CREATE_USER_URL = '/auth/registration/'
TOKEN_URL = '/auth/login/'


class PublicUserApiTest(APITestCase):
    """Test the user api public authentication"""

    def test_create_valid_user_success(self):
        payload = {
            'username': 'teos',
            'email': 'teos@teos.com',
            'password1': 'foobar123',
            'password2': 'foobar123'
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(username=payload['username'])
        self.assertTrue(user.check_password(payload['password1']))
        self.assertNotIn('password', res.data)

    def test_user_exist(self):
        """Test creating user that already exists"""
        payload1 = {
            'username': 'teos',
            'email': 'test@teos.com',
            'password': 'foobar123',
        }

        payload2 = {
            'username': 'teos',
            'email': 'test@teos.com',
            'password1': 'foobar123',
            'password2': 'foobar123'
        }

        create_user(**payload1)

        res = self.client.post(CREATE_USER_URL, payload2)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test that password must be more than 7 characters"""
        payload = {
            'username': 'teos',
            'email': 'test@teos.com',
            'password1': 'foo',
            'password1': 'foo'
        }

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exist = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exist)

    def test_create_token_for_user(self):
        """Test that a token created for user"""
        payload = {
            'username': 'teos',
            'email': 'test@teos.com',
            'password': 'foobar123',
        }

        create_user(**payload)
        res = self.client.post(TOKEN_URL, {
            'username': payload['username'],
            'password': payload['password']
        })
        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_credential(self):
        """Test that token is not created when
           invalid credential are given"""
        payload = {
            'username': 'teos',
            'email': 'test@teos.com',
            'password': 'foobar123',
        }
        create_user(**payload)

        payload2 = {
            'username': 'teos',
            'password': 'wrong123'
        }

        res = self.client.post(TOKEN_URL, payload2)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_user(self):
        """Test that token is not created if user doesn't exists"""
        payload = {
            'username': 'testusername',
            'password': 'testpass'
        }

        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_field(self):
        """Test that email and password are required"""

        res = self.client.post(TOKEN_URL, {
            'username': 'one',
            'email': '',
            'password': ''
        })

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
