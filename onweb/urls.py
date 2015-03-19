from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'onweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'notes.views.home', name='home'),
    url(r'^login/$', 'notes.views.login_view', name='login'),
    url(r'^logout/$', 'notes.views.logout_view', name='logout'),
    url(r'^register/$', 'notes.views.register', name='register'),
    url(r'^add_note/$', 'notes.views.add_note', name='add_note'),
#     url(r'^add_category/$', 'notes.views.home', name='add_category'),
    url(r'^notes/(?P<category_slug>[\w\-]+)/$', 'notes.views.notes_by_category', name='view_notes_by_category'),
    url(r'^delete_category/(?P<category_slug>[\w\-]+)/$', 'notes.views.delete_category', name='delete_category'),
    url(r'^delete_note/(?P<note_slug>[\w\-]+)/$', 'notes.views.delete_note', name='delete_note'),
    url(r'^settings/$', 'notes.views.settings', name='settings'),
    url(r'^reminders/$', 'notes.views.reminders', name='reminders'),
    url(r'^trash/$', 'notes.views.trash', name='trash'),
    url(r'^uncategorized/$', 'notes.views.uncategorized', name='uncategorized'),
    url(r'^admin/', include(admin.site.urls)),
)
