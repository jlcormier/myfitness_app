# Generated by Django 3.2.2 on 2022-10-04 02:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foodlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('time', models.TimeField(blank=True, default='%H:%M', null=True)),
                ('number_servings', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
    ]
