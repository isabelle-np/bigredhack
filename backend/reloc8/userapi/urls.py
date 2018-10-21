from django.conf.urls import url
from userapi import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^client/create$', views.ClientActions.as_view(), name='client-actions'),
]

urlpatterns = format_suffix_patterns(urlpatterns)