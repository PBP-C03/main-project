# Generated by Django 4.2.4 on 2023-12-18 19:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkoutbook', '0016_alter_nota_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 12, 18, 19, 27, 54, 967325, tzinfo=datetime.timezone.utc)),
        ),
    ]
