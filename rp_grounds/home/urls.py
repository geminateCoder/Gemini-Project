from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^goals/$', views.goals, name='goals'),
    url(r'^features/$', views.features, name='features'),
    url(r'^staff/$', views.staff, name='staff'),
    url(r'^news/$', views.news, name='news'),
]
