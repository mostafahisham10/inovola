from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Machine)
admin.site.register(Pod)

admin.site.site_header = "Inovola-task Admin"
admin.site.site_title = "Inovola-task Admin area"
admin.site.index_title = "Welcome to the Inovola-task Admin area"
