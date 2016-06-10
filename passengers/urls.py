from django.conf.urls import url
from .views import passenger_list, passenger_by_id, passenger_add_new


urlpatterns = [
    url(r'^list/$', passenger_list, name='passengers'),
    url(r'^(?P<passenger_id>\d+)/$', passenger_by_id, name='passenger_by_id'),
    url(r'^register/$', passenger_add_new, name='passenger_register'),
]