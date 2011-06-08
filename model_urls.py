from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    (r'^vote/?$', 'MyApp.views.view_vote'),
    (r'^$', 'MyApp.views.view_index'),
    (r'^(?P<slug>[\w-]+)/?$', 'MyApp.views.view_item'),
    (r'^create/?$', 'MyApp.views.create_item'),
)
