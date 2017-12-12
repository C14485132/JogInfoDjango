from django.conf.urls import url

from . import views

urlpatterns = [
    url('all', views.jog_list, name='index'),
    url(r'^(?P<pk>[0-9]+)', views.datapoints_list),
    url('put', views.new_jog)
]