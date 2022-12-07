from django.db import models
from django.urls import reverse
import uuid


# Create your models here.

class Order(models.Model):
    order_time = models.DateTimeField()
    order_station = models.ForeignKey('Station', on_delete=models.SET_NULL, null=True)  # 站點資訊
    order_user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)  # 使用者
    order_car = models.ForeignKey('Car', on_delete=models.SET_NULL, null=True)  # 車輛資訊

    order_st = (
        ('p', '未付款'),
        ('np', '已付款'),
    )
    order_status = models.CharField(
        max_length=10,
        choices=order_st,
        default='np',
    )

    def __str__(self):
        """String for representing the Model object."""
        return str(self.id)

class User(models.Model):
    user_name = models.CharField(max_length=20)
    account = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    birthday = models.DateField()

    SEX = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('n', 'None'),
    )

    sex = models.CharField(
        max_length=1,
        choices=SEX,
        default='m',
    )
    telephone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return self.user_name


class CarType(models.Model):
    type_name = models.CharField(max_length=10)
    type_number = models.IntegerField()

    def __str__(self):
        """String for representing the Model object."""
        return self.type_name


class Car(models.Model):
    st = (
        ('n', '正常'),
        ('r', '已預訂'),
        ('l', '借出中'),
        ('m', '維修中'),
    )
    status = models.CharField(
        max_length=10,
        choices=st,
        default='n',
    )
    production_time = models.DateField()
    manufacturer = models.CharField(max_length=20)
    Insurance_id = models.CharField(max_length=50)
    car_type = models.ForeignKey('CarType', on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('car-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return str(self.id)


class Station(models.Model):
    station_name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    maximum_load = models.IntegerField(blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.station_name
class Report(models.Model):
    reason = models.TextField(max_length=1000)
    date = models.DateTimeField()

    def __str__(self):
        """String for representing the Model object."""
        return str(self.id)

