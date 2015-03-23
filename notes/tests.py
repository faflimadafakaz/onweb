from django.test import TestCase
from django.test import Client

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from _mysql import IntegrityError

# Create your tests here.
class LinkTestCase(TestCase):
    client = Client()
    def test_the_correct_links_work(self, client=client):
        links = ['/', '/reminders/', '/trash/','/settings/']
        redirect = ['/login/','/logout/','/register/','/delete_note/this-note/']
        for link in links:
            response = client.get(link)
            self.assertEqual(response.status_code, 200, 'link '+link+str(response.status_code))
        for link in redirect:
            response = client.get(link)
            self.assertEqual(response.status_code, 302, 'link '+link+str(response.status_code))
            
    def test_incorrect_links_give_404(self, client= client):
        links=['/home/?page=1/', '/login/3030/', '/add-note/suraj-3-3-username/']
        for link in links:
            response = client.get(link)
            self.assertEqual(response.status_code, 404, "link %s is valid "%(link))
    
    def test_add_user(self, client=client):
        '''
        create a new user with each user having a distinct username and a distinct emailID
        '''
        names = ['_ransom_', 'select_*', 'another_random_user','thept']
        for i in names:
            user = User()
            user.username=i
            user.email=i+'@gmail.com'
            self.assertRaises(IntegrityError, user.save())
            
    def test_links_should_only_on_login(self, client=client):
        links = ['/logout/','/edit_note/samplenote', '/notes/diary', '/delete_category/diary', '/delete_note/samplenote']
        
        for link in links:
            response = client.get(link)
            self.assertEqual(response.status_code, 302, "link "+link+ " "+str(response.status_code))