from django.db import models
from django.db.models.fields.related import OneToOneField, ForeignKey

from datetime import datetime
from django.utils.text import slugify

from django.contrib.auth.models import User

# Create your models here.
   
class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=50)
    user = models.ForeignKey(User)
    #colour = models.IntegerField(required=False)

    
    def __unicode__(self):
        return self.name
    

class Notes(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category)
    user = models.ForeignKey(User)
    #reminder = models.DateTimeField(default='',null=True)
    permalink = models.CharField(max_length=50, null=False, unique=True)
    
    def __unicode__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.modified = datetime.now()
        super(Notes, self).save(*args, **kwargs)