# Generated by Django 4.1.2 on 2022-10-25 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Goods",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "version",
                    models.CharField(max_length=50, unique=True, verbose_name="型号"),
                ),
                (
                    "cost",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="成本"
                    ),
                ),
                (
                    "rp",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="参考价格"
                    ),
                ),
                (
                    "mul",
                    models.CharField(
                        blank=True, max_length=128, null=True, verbose_name="倍数"
                    ),
                ),
                (
                    "search",
                    models.CharField(
                        blank=True, max_length=128, null=True, verbose_name="正能量搜索次数"
                    ),
                ),
                (
                    "cloudp",
                    models.CharField(
                        blank=True, max_length=128, null=True, verbose_name="云价格次数"
                    ),
                ),
                (
                    "ic_same",
                    models.CharField(
                        blank=True, max_length=128, null=True, verbose_name="IC网同行数"
                    ),
                ),
                (
                    "ic_now",
                    models.CharField(
                        blank=True, max_length=128, null=True, verbose_name="IC网现货数"
                    ),
                ),
                (
                    "same_now",
                    models.CharField(
                        blank=True, max_length=128, null=True, verbose_name="同行现货变化"
                    ),
                ),
                (
                    "clouds",
                    models.CharField(
                        blank=True, max_length=128, null=True, verbose_name="云汉商城情况"
                    ),
                ),
                (
                    "user",
                    models.CharField(
                        blank=True, max_length=128, null=True, verbose_name="评估人"
                    ),
                ),
                (
                    "detail",
                    models.CharField(
                        blank=True, max_length=128, null=True, verbose_name="料号说明"
                    ),
                ),
                (
                    "total",
                    models.CharField(
                        blank=True, max_length=128, null=True, verbose_name="总分"
                    ),
                ),
                (
                    "state",
                    models.CharField(
                        choices=[("审核中", "审核中"), ("通过", "通过"), ("不通过", "不通过")],
                        default="审核中",
                        max_length=128,
                        verbose_name="状态",
                    ),
                ),
                (
                    "grade",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("A", "A级"),
                            ("B", "B级"),
                            ("C", "C级"),
                            ("D", "D级"),
                            ("E", "E级"),
                            ("F", "F级"),
                        ],
                        max_length=128,
                        null=True,
                        verbose_name="评级",
                    ),
                ),
            ],
            options={"verbose_name": "物料", "verbose_name_plural": "物料",},
        ),
    ]
