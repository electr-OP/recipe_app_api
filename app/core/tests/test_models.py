from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@gmail.com'
        password = '1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_normalizes(self):
        email = 'test@gMail.com'
        user = get_user_model().objects.create_user(email)
        self.assertEqual(user.email, email.lower())

    def test_email_address_given(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None)

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'supertest@gmail.com', '12345'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
