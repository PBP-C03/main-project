# Generated by Django 4.2.5 on 2023-10-27 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkoutbook', '0001_initial'),
        ('cartbook', '0003_book_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_cart',
            name='nota',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='checkoutbook.nota'),
        ),
        migrations.AlterField(
            model_name='book_cart',
            name='carts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cartbook.cart'),
        ),
    ]
