from django.test import TestCase
from .models import Project,Profile
from django.contrib.auth.models import User


# Create your tests here.
class ProfileTestClass(TestCase):
    '''
    Tests for the profile class
    '''
    def setUp(self):
        self.profile=Profile(user=user,profile_pic="profile_pic_url",bio="test user",email='test2@gmail.com')

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        self.profile.delete_profile()
        profiles= Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

class ProjectTestClass(TestCase):
    '''
    Tests  for the projects class
    '''
    def setUp(self):
        self.test2 = User(username="test2", email="test2@gmail.com", password = "12345")
        self.test = Project(project_name= "test", project_screenshot = "project_screenshot_url", project_description ="test project", project_url = "testlink", profile= self.test2)

        self.test2.save()
        self.test.save_project()

    def tearDown(self):
        Project.objects.all().delete()

    def test_image_instance(self):
        self.assertTrue(isinstance(self.test, Project))

    def test_save_project_method(self):
        self.test.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)> 0)

    def test_delete_project(self):
        self.test.save_project()
        projects1 = Project.objects.all()
        self.assertEqual(len(projects1),1)
        self.test.delete_project()
        projects2 = Project.objects.all()
        self.assertEqual(len(projects2),0)

    def test_display_projects(self):
        projects = Project.display_all_projects()
        self.assertTrue(len(projects) > 0 )

    def test_search_project(self):
        self.test.save_project()
        project = Project.search_project(self.test.project_name)
        self.assertEqual(len(project),1)

    def test_get_user_projects_(self):
        self.test.save_project()
        self.test2.save()
        profile_projects = Project.get_user_projects(self.test2)
        self.assertEqual(len(profile_projects),1 )