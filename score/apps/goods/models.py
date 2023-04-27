from django.db import models

# Create your models here.


class Goods(models.Model):
    """
    物料
    """
    version = models.CharField(max_length=50, unique=True, verbose_name="型号")  # unique=True, 这个字段在表中必须有唯一值.
    x1 = models.CharField(max_length=128,verbose_name="小型包装型号", null=True, blank=True)
    x2 = models.CharField(max_length=128, verbose_name="小型包装型号2", null=True, blank=True)
    cost = models.CharField(max_length=50, null=True, blank=True,  verbose_name="成本")
    rp = models.CharField(max_length=50, null=True, blank=True, verbose_name="参考价格")
    mul = models.CharField(max_length=128,  null=True, blank=True, verbose_name="倍数")
    search = models.CharField(max_length=128, null=True, blank=True, verbose_name="正能量搜索次数")
    cloudp = models.CharField(max_length=128, null=True, blank=True, verbose_name="云价格次数")
    ic_same = models.CharField(max_length=128, null=True, blank=True, verbose_name="IC网现货排名商家")
    ic_now = models.CharField(max_length=128, null=True, blank=True, verbose_name="IC网现货数")
    same_now = models.CharField(max_length=128, null=True, blank=True, verbose_name="同行现货变化")
    clouds = models.CharField(max_length=128, null=True, blank=True, verbose_name="云汉商城情况")
    user = models.CharField(max_length=128, null=True, blank=True, verbose_name="评估人")
    detail = models.CharField(max_length=256, null=True, blank=True, verbose_name="料号说明")
    total = models.IntegerField(max_length=128, null=True, blank=True, verbose_name="总分")
    state = models.CharField(max_length=128, verbose_name="状态", choices=(('审核中', '审核中'),
                                                                            ('通过', '通过'),
                                                                            ('不通过', '不通过')), default='审核中')
    grade = models.CharField(max_length=128, verbose_name="评级", choices=(('A', 'A级'), ('B', 'B级'), ('C', 'C级'),
                                                                           ('D', 'D级'),
                                                                           ('E', 'E级'), ('F', 'F级')),
                             null=True, blank=True)
    add_time = models.CharField(max_length=128, verbose_name="添加时间", null=True, blank=True)

    def __str__(self):
        return self.version

    class Meta:
        verbose_name = '物料'
        verbose_name_plural = verbose_name