# Generated by Django 4.1.3 on 2022-12-13 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_rent', '0007_order_order_station_transaction_transaction_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='status',
            field=models.CharField(choices=[('正常', '正常'), ('已預訂', '已預訂'), ('借出中', '借出中'), ('維修中', '維修中')], default='正常', max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('未付款', '未付款'), ('已付款', '已付款')], default='未付款', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='account',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('男', 'Male'), ('女', 'Female'), ('無', 'None')], default='男', max_length=1),
        ),
    ]
