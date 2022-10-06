from django.urls import include, re_path
from .views import *
urlpatterns = [
    re_path(r'^musica_list/', musica_list, name='musica_list'),
    re_path(r'^musica_new/', musica_new, name='musica_new'),

]