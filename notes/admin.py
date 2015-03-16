from django.contrib import admin
from notes.models import Notes, Category
# Register your models here.

admin.site.register(Notes)
admin.site.register(Category)