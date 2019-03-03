from django.conf.urls import url
from django.conf.urls.static import static
from Herois import settings
from django.contrib import admin
from django.views.static import serve

from pagina import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^upload/', views.model_upload, name='model_upload'),
    url(r'^edit/(?P<pk>\d+)', views.model_edit, name='model_edit'),
    url(r'^delete/(?P<pk>\d+)', views.model_delete, name='model_delete'),
    url(r'^add_favorites/(?P<pk>\d+)', views.add_favorites, name='add_favorites'),
    url(r'^favoritos/', views.favoritos, name='favoritos'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
