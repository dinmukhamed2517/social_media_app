from django.urls import path
from api import views
urlpatterns = [
    path('', views.home, name='home'),
    path('profile_list', views.profile_list, name='profile_list'),
    path('profile/<int:id>', views.profile, name='profile')
]
