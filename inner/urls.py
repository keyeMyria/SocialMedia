from django.conf.urls import url 
from .views import *
urlpatterns=[
url(r'pass',passcheck,name="password check"),
url(r'look',look_for_users,name="look_for_someone"),
url(r'pic_im1',pic_im1,name="profile picture"),
url(r'pic_im2',pic_im2,name="cover picture"),
url(r'pic',pic,name="change cover and profile pic"),
url(r'post/poste',poste,name="post effected"),
url(r'post/id_im1',im_id,name="image with id"),
url(r'post/load_site',load_site,name="image with id"),
url(r'post/load_posts',status,name="laod postes"),

]
