from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.run_list, name='index'),
]