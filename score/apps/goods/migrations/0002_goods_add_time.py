# Generated by Django 4.1.2 on 2022-10-25 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("goods", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="goods",
            name="add_time",
            field=models.CharField(
                blank=True, max_length=128, null=True, verbose_name="添加时间"
            ),
        ),
    ]
