from django.conf.urls import url
from . import views

app_name = 'rents'

urlpatterns = [
    url(r'^add_rent/$', views.add_rent, name="add_rent"),
    url(r'^modify_rent/$', views.modify_rent, name="modify"),
    url(r'^(?P<id>[0-9]+)/$', views.rent_details, name="detail"),
    url(r'^$', views.list_rents, name="list"),
]
