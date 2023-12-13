from django.contrib import admin

from .models import Bus,Route,Schedule,Booking

# Register your models here.
admin.site.register(Bus)
admin.site.register(Route)
admin.site.register(Schedule)
admin.site.register(Booking)