from django.urls import path
from users.views import register, login,password,user_card,logout


urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('password', password, name='password'),
    path('user', user_card, name='user'),
]
