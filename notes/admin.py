from django.contrib import admin
from notes.models import Notes, Category, UserProfile
# Register your models here.

admin.site.register(Notes)
admin.site.register(Category)
admin.site.register(UserProfile)