from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('home/',include("home.urls"))
=======
    path('home/', include('home.urls'))
>>>>>>> 2406a6d00075102e539af58ce1ed85d4010d60d2
]
