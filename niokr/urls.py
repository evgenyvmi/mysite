from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^login/$', views.post_login, name='post_login'),
    url(r'^request/$', views.create_request, name='create_request'),
    url(r'^expert/$', views.expert, name='expert'),
    url(r'^logout/$', views.logout_view, name='logout')
]