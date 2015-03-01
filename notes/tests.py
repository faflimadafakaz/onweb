from django.test import TestCase
from django.test import Client

from django.core.urlresolvers import reverse

# Create your tests here.
class LinkTestCase(TestCase):
    client = Client()
    def test_the_correct_links_work(self, client=client):
        links = ['/', '/login/', '/logout/', '/reminders/', '/register/','/add_note/this-note/','/delete_note/this-note/']
        for link in links:
            response = client.get(link)
            self.assertEqual(response.status_code, 200, 'link'+link)
            
    def test_incorrect_links_give_404(self, client= client):
        links=['/home/?page=1/', '/login/3030/', '/add-note/suraj-3-3-username/']
        for link in links:
            response = client.get(link)
            self.assertEqual(response.status_code, 404, "link %s is valid "%(link))
        self.fail("you have to do the db models, login/logout, ajax")