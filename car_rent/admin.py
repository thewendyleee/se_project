from django.contrib import admin
from .models import *


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('account', 'user_name', 'birthday', 'sex', 'telephone', 'address')


admin.site.register(User, UserAdmin)


class CarTypeAdmin(admin.ModelAdmin):
    list_display = ('id','type_name', 'type_number')


admin.site.register(CarType, CarTypeAdmin)


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'manufacturer', 'production_time', 'Insurance_id', 'car_type', 'locate_station')


admin.site.register(Car, CarAdmin)


class StationAdmin(admin.ModelAdmin):
    list_display = ('station_name', 'address', 'maximum_load')


admin.site.register(Station, StationAdmin)


class UserOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_car', 'order_use_time', 'order_return_time',  'order_user', 'order_station', 'order_status')


admin.site.register(Order, UserOrderAdmin)


class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'reason', 'date')


admin.site.register(Report, ReportAdmin)


class TransactionAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'pick_up_car_time', 'return_car_time', 'transaction_user', 'transaction_car', 'transaction_station', 'pay')


admin.site.register(Transaction, TransactionAdmin)
