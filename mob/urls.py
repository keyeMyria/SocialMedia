from django.conf.urls import url 
from .views import *


urlpatterns=[
url(r"^$", download),
url(r"^files$", download_list),
url(r"^file$", download_file),
]