from django.conf.urls import url
from .views import route_list, route_by_id, route_list_by_passenger


urlpatterns = [
    url(r'^list/$', route_list, name='routes'),
    url(r'^(?P<route_id>\d+)/$', route_by_id, name='route_by_id'),
    url(r'^passenger/(?P<passenger_id>\d+)/$', route_list_by_passenger, name='routes_by_passenger'),
]