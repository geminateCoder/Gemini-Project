from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^profile/(?P<id>[\w-]+)/$', views.userProfile, name='user_profile'),
    url(r'^settings/$', views.update_profile, name='update_profile'),
    url(r'^dashboard/$', views.dashboard, name='user_dash'),

]