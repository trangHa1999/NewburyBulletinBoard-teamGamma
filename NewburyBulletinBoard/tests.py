from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

class HomePageTests(SimpleTestCase):
    def test_homePageStatusCode(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_viewUrlByName(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_viewUsesCorrectTemplate(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/index.html')

class SignupPageTests(TestCase):
    username = 'newuser'
    email = 'newuser@email.com'
    age = 27

    def test_signupPageStatusCode(self):
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)

    def test_viewUrlByName(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_viewUsesCorrectTemplate(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/signup.html')

    def test_signup_form(self):
        testNewUser = get_user_model().objects.create_user(self.username, self.email, self.age)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all() [0].username, self.username)
        self.assertEqual(get_user_model().objects.all() [0].email, self.email)
        # self.assertEqual(get_user_model().objects.all() [0].age, self.age)