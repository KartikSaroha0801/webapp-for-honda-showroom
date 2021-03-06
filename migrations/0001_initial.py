# Generated by Django 4.0.4 on 2022-05-07 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookingbycustomer',
            fields=[
                ('custid', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Bookingbystaff',
            fields=[
                ('Bookingid', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('Custname', models.CharField(max_length=50)),
                ('Custid', models.IntegerField(primary_key=True, serialize=False)),
                ('Address', models.CharField(max_length=50)),
                ('PanCard', models.CharField(max_length=50)),
                ('AdharcardNo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Staffname', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=50)),
                ('PanCard', models.CharField(max_length=50)),
                ('AdharcardNo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VehicleType', models.CharField(max_length=50)),
                ('Company', models.CharField(max_length=50)),
            ],
        ),
    ]
