# Generated by Django 4.1.2 on 2022-10-25 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("goods", "0004_goods_x1"),
    ]

    operations = [
        migrations.AlterField(
            model_name="goods",
            name="ic_same",
            field=models.CharField(
                blank=True, max_length=128, null=True, verbose_name="IC网现货排名商家"
            ),
        ),
    ]
