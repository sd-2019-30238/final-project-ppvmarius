from django.conf.urls import url
from . import views

app_name = 'cars'

urlpatterns = [
    url(r'^$', views.car_list, name="list"),
    url(r'^(?P<slug>[\w-]+)/$', views.car_detail, name="detail"),
]
