from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage,name='login'),
    path('register/',views.registerPage,name='register'),
    path('logout/',views.logoutUser,name='logout'),
    path('',views.home,name="home"),
    path('player/<str:pk>',views.player,name="player"),
    path('user-profile/<str:pk>',views.userProfile,name="user-profile"),
    
    path('create-player/',views.createPlayer, name='create-player'),
    path('update-player/<str:pk>',views.updatePlayer, name='update-player'),
    path('delete-player/<str:pk>',views.deletePlayer, name='delete-player')
    
]