from django.conf.urls import url
from . import views
from .views import DelChara

urlpatterns = [
    url(r'^profile/(?P<id>\d+)/$', views.charaProfile, name='chara_profile'),
        url(r'^edit/(?P<id>\d+)/$', views.charaEdit, name='chara_edit'),
    url(r'^create/$', views.charaCreate, name='create'),
    url(r'^archive/$', views.charaArchive, name='archive'),
    url(r'^favorites/$', views.favChara, name='favchara'),
    url(r'^delete/(?P<pk>\d+)/$', DelChara.as_view(), name='delchara'),
]