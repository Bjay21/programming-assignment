from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from blog import views

app_name ="blog"
urlpatterns = [
    url(r'^post/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<post_pk>\d+)/comments/new/$', views.comment_new, name="comments"),
]