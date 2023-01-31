from django.urls import path
from .views import person_view

app_name = 'humans'

urlpatterns = [
    path('person/<int:pk>', person_view, name='person_view'),
]