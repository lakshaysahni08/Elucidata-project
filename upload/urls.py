from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='upload'

urlpatterns = [
    url(r'^$', views.upload, name='upload'),
    url(r'^filter/$', views.filter_compound, name='filter'),
    url(r'^round/$', views.round_time, name='round'),
    url(r'^mean/$', views.mean_finder, name='mean'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)