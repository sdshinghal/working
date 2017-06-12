from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from gapyear import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page')
]