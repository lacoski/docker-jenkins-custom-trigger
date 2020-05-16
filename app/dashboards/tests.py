from django.test import TestCase
from dashboards.models import Blog

# Create your tests here.

class DemoTestCase(TestCase):
    def setUp(self):
        Blog.objects.create(name="Demo 123", title="This is demo 123")
        Blog.objects.create(name="Demo 321", title="This is demo 321")

    def test_case_1(self):
        blog_1 = Blog.objects.get(name="Demo 123")
        blog_2 = Blog.objects.get(name="Demo 321")
        self.assertEqual(blog_1.title, "This is demo 123")
        self.assertEqual(blog_2.title, "This is demo 321")

    def test_case_2(self):
        blog_1 = Blog.objects.get(name="Demo 123")
        blog_2 = Blog.objects.get(name="Demo 321")
        self.assertEqual(blog_1.title, "This is demo 123")
        self.assertEqual(blog_2.title, "This is demo 321")

    def test_case_3(self):
        blog_1 = Blog.objects.get(name="Demo 123")
        blog_2 = Blog.objects.get(name="Demo 321")
        self.assertEqual(blog_1.title, "This is demo 123")
        self.assertEqual(blog_2.title, "This is demo 321")

    def test_case_4(self):
        blog_1 = Blog.objects.get(name="Demo 123")
        blog_2 = Blog.objects.get(name="Demo 321")
        self.assertEqual(blog_1.title, "This is demo 123")
        self.assertEqual(blog_2.title, "This is demo 321")
