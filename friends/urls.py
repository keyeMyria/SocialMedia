from django.conf.urls import url 
from .views import *


urlpatterns=[
url(r'^request',reqst),
url(r'^respond',respond),
url(r'^update',update),
]