from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'onweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'notes.views.home', name='home'),
    url(r'^login/$', 'notes.views.login', name='login'),
    url(r'^logout/$', 'notes.views.logout', name='logout'),
    url(r'^register/', 'notes.views.register', name='register'),
    url(r'^add_note/(?P<note_slug>[\w\-]+)/$', 'notes.views.add_note', name='add_note'),
    url(r'^delete_note/(?P<note_slug>[\w\-]+)/$', 'notes.views.delete_note', name='delete_note'),
    url(r'^settings/$', 'notes.views.settings', name='settings'),
    url(r'^reminders/$', 'notes.views.reminders', name='reminders'),
    url(r'^trash/$', 'notes.views.trash', name='trash'),
    url(r'^uncategorized/$', 'notes.views.uncategorized', name='uncategorized'),
)
