from django.conf.urls import patterns, include, url
from whatprivilege import views
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^question/$', views.question, name='question'),
    url(r'^instructions/$', views.instructions, name='instructions'),
    url(r'^workshop-code/$', views.makeWorkshop, name='workshop'),   
# url(r'^answer/(number)/$', 'views.answer', name='answer')
)
