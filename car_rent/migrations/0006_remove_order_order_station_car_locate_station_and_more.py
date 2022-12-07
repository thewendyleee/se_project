# Generated by Django 4.1.3 on 2022-12-07 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_rent', '0005_transaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_station',
        ),
        migrations.AddField(
            model_name='car',
            name='locate_station',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='car_rent.station'),
        ),
        migrations.AddField(
            model_name='report',
            name='report_car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='car_rent.car'),
        ),
        migrations.AddField(
            model_name='report',
            name='report_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='car_rent.user'),
        ),
        migrations.AlterField(
            model_name='cartype',
            name='type_name',
            field=models.CharField(max_length=20),
        ),
    ]
