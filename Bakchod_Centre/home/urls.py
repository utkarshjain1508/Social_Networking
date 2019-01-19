from . import views
from django.urls import path

urlpatterns = [
    path('', views.index1,name="index1"),
    path('signup',views.index2,name="index2"),
    path('user',views.index3,name="index3"),
    path('user/edit',views.index4,name="index4"),
]
