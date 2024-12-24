from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

app_name = 'ekz'
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='store/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('profile/<str:username>/', views.profile, name='profile'),

    path('catalog/', views.catalog, name='catalog')
]