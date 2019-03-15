from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Connection)
admin.site.register(Post)
# Register your models here.
