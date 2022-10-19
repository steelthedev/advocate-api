from django.urls import path
from . import views

urlpatterns=[
    path('', views.DeveloperListView.as_view())
]