from . import views
from django.urls import path

urlpatterns = [
    path('', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('username', views.profile, name='profile'),
    path('username/edit', views.UserEdit.as_view(), name='useredit'),
]
