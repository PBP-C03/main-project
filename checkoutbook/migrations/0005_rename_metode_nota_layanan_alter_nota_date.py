# Generated by Django 4.2.5 on 2023-10-29 14:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkoutbook', '0004_alter_nota_alamat_alter_nota_date_alter_nota_metode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nota',
            old_name='metode',
            new_name='layanan',
        ),
        migrations.AlterField(
            model_name='nota',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 10, 29, 14, 6, 32, 897708, tzinfo=datetime.timezone.utc)),
        ),
    ]
