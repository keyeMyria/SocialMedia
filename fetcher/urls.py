from django.conf.urls import url 
from views import *

urlpatterns=[
url(r"^$", index_pattern),
url(r"^ini_job$",ini_Pattern),
url(r"^get_job$",check_result),

]
