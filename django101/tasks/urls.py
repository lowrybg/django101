from django.urls import path

from django101.tasks.views import my_view, home

urlpatterns = (
    path('g/', home )
)
