# Generated by Django 4.2.5 on 2023-11-20 08:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkoutbook', '0012_alter_nota_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 11, 20, 8, 58, 6, 398090, tzinfo=datetime.timezone.utc)),
        ),
    ]
