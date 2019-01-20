<<<<<<< HEAD
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name="index"),
]
=======
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
>>>>>>> 2406a6d00075102e539af58ce1ed85d4010d60d2
