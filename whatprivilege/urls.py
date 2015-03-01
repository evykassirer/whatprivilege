from django.conf.urls import patterns, url
from whatprivilege import views

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^question/$', views.question, name='question'),
    url(r'^instructions/$', views.instructions, name='instructions'),
    url(r'^workshop-code/$', views.makeWorkshop, name='workshop'),
    url(r'^(?P<code>[\da-z0-9]+)/$', views.loadWorkshop,
        name='load_workshop'),
)

handler404 = "views.error404"
