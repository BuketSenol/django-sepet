# Generated by Django 4.2.2 on 2023-07-27 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0003_shopcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopcard',
            name='totalPrice',
            field=models.IntegerField(editable=False, verbose_name='Toplam Fiyat'),
        ),
    ]