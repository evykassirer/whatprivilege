from django.conf.urls import patterns, include, url
from whatprivilege import views
urlpatterns = patterns('',
    url(r'^$', 'views.home', name='home'),
    url(r'^instructions/$', name='instructions')    
# url(r'^answer/(number)/$', 'views.answer', name='answer')
)
