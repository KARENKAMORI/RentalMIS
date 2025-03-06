from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.index, name="index"),
    path('', views.home, name="home"),
    path('tenant/', views.dashboard, name="dashboard"),
    path('houseSearch/', views.search_house, name="houseSearch"),
]