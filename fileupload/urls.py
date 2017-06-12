from django.conf.urls import url, include
# from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include


urlpatterns = [
    url(r'^$', views.ListFile.as_view(), name='ListFile'),
    url(r'^(?P<pk>[0-9]+)/$', views.FileDetail.as_view()),
    url(r'^upload/$', views.FileUploadView.as_view()),
    # url(r'^upload/(?P<filename>[^/]+)$', views.FileUploadView.as_view()),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = format_suffix_patterns(urlpatterns)
