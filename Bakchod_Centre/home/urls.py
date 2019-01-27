from . import views
from django.urls import path

app_name = 'home'

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('signup', views.signup, name='signup'),
    path('username', views.profile, name='profile'),
    path('username/edit', views.user_edit, name='user_edit'),
]
