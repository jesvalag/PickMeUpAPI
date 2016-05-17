from django.conf.urls import url
from .views import passenger_list


urlpatterns = [
    url(r'^list/$', passenger_list, name='passenger_list'),
]