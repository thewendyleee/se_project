from django.contrib import admin
from .models import *


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'id', 'account')


admin.site.register(User, UserAdmin)


class CarTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name', 'type_number')


admin.site.register(CarType, CarTypeAdmin)


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'manufacturer', 'car_type')


admin.site.register(Car, CarAdmin)


class StationAdmin(admin.ModelAdmin):
    list_display = ('station_name', 'address', 'maximum_load')


admin.site.register(Station, StationAdmin)


class UserOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_car', 'order_user', 'order_station')


admin.site.register(Order,UserOrderAdmin)


class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'reason', 'date')


admin.site.register(Report, ReportAdmin)
