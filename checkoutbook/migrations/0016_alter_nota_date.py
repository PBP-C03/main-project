# Generated by Django 4.2.4 on 2023-12-01 12:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkoutbook', '0015_alter_nota_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 12, 1, 12, 37, 7, 482516, tzinfo=datetime.timezone.utc)),
        ),
    ]
