# Generated by Django 2.0.4 on 2018-04-12 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_cart'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': '用户购物车', 'verbose_name_plural': '用户购物车'},
        ),
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='价格'),
        ),
    ]
