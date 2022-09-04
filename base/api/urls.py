from django.urls import path
from . import views
urlpatterns = [
    path('',views.getRoutes),
    path('players/', views.getPlayers),
    path('players/<int:pk>', views.getPlayer)
]