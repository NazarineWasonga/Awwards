from django.test import TestCase

# Create your tests here.
from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Projects,Profile,Review
from django.contrib.auth.models import User
# Create your tests here.


class ProjectsTestClass(TestCase):
    #set up method
    def setUp(self):
        self.nazzy = Projects(title='nazryn',description="nazz",location="kibra",image = 'media/projects/acefamily.jpg')
    #testing instance

    def test_instance(self):
        self.assertTrue(isinstance(self.nazzy, Projects))
    #testing save method

    def test_save_method(self):
        self.nazzy.save_project()
        projects = Projects.objects.all()
        self.assertTrue(len(projects) > 0)
    #testng for deleting method

    def test_delete_method(self):
        self.nazzy.save_project()
        self.nazzy.delete_project()
        projects = Projects.objects.all()
        self.assertFalse(len(projects) == 1)

    def test_update_method(self):
        self.nazzy.save_project()
        self.nazzy.update_project()
        projects = Projects.objects.all()
        self.assertTrue(len(projects) > 0)    

class ProfileTestClass(TestCase):
    def setUp(self):
        self.posts = Profile(contact='nazryn',bio="nazryne",profile_pic = 'media/projects/acefamily.jpg')
    #testing instance

    def test_instance(self):
        self.assertTrue(isinstance(self.posts, Profile))
    #testing save method

    def test_save_method(self):
        self.posts.save_profile()
        postss = Profile.objects.all()
        self.assertTrue(len(postss) > 0)
    # #testng for deleting method

    def test_delete_method(self):
        self.posts.save_profile()
        self.posts.delete_profile()
        postss = Profile.objects.all()
        self.assertFalse(len(postss) == 1)

class ReviewTestClass(TestCase):
    def setUp(self):
        self.nazryn= Review(user_name = "good trial",comment="fine",rating=1)
    #testing instance

    def test_instance(self):
        self.assertTrue(isinstance(self.nazryn, Review))
    #testing save method

    def test_save_method(self):
        self.nazryn.save_review()
        coment = Review.objects.all()
        self.assertTrue(len(coment) > 0)
    # # #testng for deleting method

    def test_delete_method(self):
        self.nazryn.save_review()
        self.nazryn.delete_review()
        coment = Review.objects.all()
        self.assertFalse(len(coment) == 1)        










