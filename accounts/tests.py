from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model(self)
        user = User.objects.create_user(
            username='will', email='will@email.com', password='testpass123'
        )
        self.assertEqual(user.username, 'will')
        self.assetEqual(user.email, 'will@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

