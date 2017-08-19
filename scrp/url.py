from django.conf.urls import url , include
from .views import pattern
urlpatterns= [
url(r'^post$',pattern,name="post pattern"),

]