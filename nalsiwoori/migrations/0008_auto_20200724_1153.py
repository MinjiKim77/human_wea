# Generated by Django 3.0.3 on 2020-07-24 02:53

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nalsiwoori', '0007_auto_20200724_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selection',
            name='map_data',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nalsiwoori.map_data'),
        ),
        migrations.AlterField(
            model_name='selection',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 24, 2, 53, 45, 984585, tzinfo=utc)),
        ),
    ]