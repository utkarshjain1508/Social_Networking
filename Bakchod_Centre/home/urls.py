from . import views
from django.urls import path

urlpatterns = [
    path('', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('user', views.profile, name="profile"),
    path('user/edit', views.UserEdit.as_view(), name="useredit"),
]
