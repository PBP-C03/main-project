# Generated by Django 4.2.5 on 2023-10-27 18:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkoutbook', '0003_nota_alamat_nota_metode_alter_nota_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='alamat',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='nota',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 10, 27, 18, 30, 1, 645178, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='nota',
            name='metode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
