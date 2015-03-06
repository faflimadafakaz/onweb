from django.db import models
from django.db.models.fields.related import OneToOneField, ForeignKey

from datetime import datetime
from django.utils.text import slugify

from django.contrib.auth.models import User

# Create your models here.
   
class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=50, primary_key=True)
    #colour = models.IntegerField(required=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return self.name
    
class UserProfile(models.Model):
    user = OneToOneField(User)
    

class Notes(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category)
    user = models.ForeignKey(UserProfile)
    #reminder = models.DateTimeField(default='',null=True)
    permalink = models.CharField(max_length=50, null=False)
    
    def __unicode__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.modified = datetime.now()
        super(Notes, self).save(*args, **kwargs)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])