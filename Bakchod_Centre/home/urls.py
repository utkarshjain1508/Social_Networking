from . import views
from django.urls import path

app_name = 'home'

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('signup', views.signup, name='signup'),
    path('<slug:userName>', views.profile, name='profile'),
    path('<slug:userName>/edit', views.user_edit, name='user_edit'),
    path('<slug:userName>/view_profile', views.user_view_profile, name='user_view_profile'),
    path('<slug:userName>/change_password', views.change_password, name='change_password'),
]
