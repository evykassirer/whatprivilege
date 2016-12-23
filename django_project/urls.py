from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('whatprivilege.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
