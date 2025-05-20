from django.urls import path, re_path
from django.conf.urls.static import static
from pagina import settings
from django.contrib import admin

from pagina import views

urlpatterns = [
    re_path(r"^$", views.home, name="home"),
    path("admin/", admin.site.urls),
    re_path(r"^upload/", views.model_upload, name="model_upload"),
    re_path(r"^edit/(?P<pk>\d+)", views.model_edit, name="model_edit"),
    re_path(r"^delete/(?P<pk>\d+)", views.model_delete, name="model_delete"),
    re_path(r"^add_favorites/(?P<pk>\d+)", views.add_favorites, name="add_favorites"),
    re_path(r"^favoritos/", views.favoritos, name="favoritos"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
