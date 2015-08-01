from django.conf.urls import patterns, url
from whatprivilege import views

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^question/$', views.question, name='question'),
    url(r'^instructions/$', views.instructions, name='instructions'),
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^so_what*', views.so_what, name='so_what'),
)

handler404 = "whatprivilege.views.error404"
