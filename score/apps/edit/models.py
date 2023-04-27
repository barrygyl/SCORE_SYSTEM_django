from django.db import models

# Create your models here.


class Mul(models.Model):
    """
    信息
    """
    lei = models.CharField(max_length=50,null=True, blank=True, verbose_name="类")
    up = models.CharField(max_length=50,null=True, blank=True, verbose_name="上限")
    down = models.CharField(max_length=50,null=True, blank=True, verbose_name="下限")
    score = models.IntegerField(max_length=50,null=True, blank=True, verbose_name="分值")

    def __str__(self):
        return self.lei

    class Meta:
        verbose_name = '倍数'
        verbose_name_plural = verbose_name


class Search(models.Model):
    """
    信息
    """
    lei = models.CharField(max_length=50,null=True, blank=True, verbose_name="类")
    up = models.CharField(max_length=50,null=True, blank=True, verbose_name="上限")
    down = models.CharField(max_length=50,null=True, blank=True, verbose_name="下限")
    score = models.IntegerField(max_length=50,null=True, blank=True, verbose_name="分值")

    def __str__(self):
        return self.lei

    class Meta:
        verbose_name = '正能量搜索次数'
        verbose_name_plural = verbose_name


class Cloudp(models.Model):
    """
    信息
    """
    lei = models.CharField(max_length=50,null=True, blank=True, verbose_name="类")
    up = models.CharField(max_length=50,null=True, blank=True, verbose_name="上限")
    down = models.CharField(max_length=50,null=True, blank=True, verbose_name="下限")
    score = models.IntegerField(max_length=50,null=True, blank=True, verbose_name="分值")

    def __str__(self):
        return self.lei

    class Meta:
        verbose_name = '云价格次数'
        verbose_name_plural = verbose_name


class Ic_same(models.Model):
    """
    信息
    """
    lei = models.CharField(max_length=50,null=True, blank=True, verbose_name="类")
    up = models.CharField(max_length=50,null=True, blank=True, verbose_name="上限")
    down = models.CharField(max_length=50,null=True, blank=True, verbose_name="下限")
    score = models.IntegerField(max_length=50,null=True, blank=True, verbose_name="分值")

    def __str__(self):
        return self.lei

    class Meta:
        verbose_name = 'IC网同行数'
        verbose_name_plural = verbose_name


class Ic_now(models.Model):
    """
    信息
    """
    lei = models.CharField(max_length=50,null=True, blank=True, verbose_name="类")
    up = models.CharField(max_length=50,null=True, blank=True, verbose_name="上限")
    down = models.CharField(max_length=50,null=True, blank=True, verbose_name="下限")
    score = models.IntegerField(max_length=50,null=True, blank=True, verbose_name="分值")

    def __str__(self):
        return self.lei

    class Meta:
        verbose_name = 'IC网现货数'
        verbose_name_plural = verbose_name


class Same_now(models.Model):
    """
    信息
    """
    lei = models.CharField(max_length=50,null=True, blank=True, verbose_name="类")
    up = models.CharField(max_length=50,null=True, blank=True, verbose_name="上限")
    down = models.CharField(max_length=50,null=True, blank=True, verbose_name="下限")
    score = models.IntegerField(max_length=50,null=True, blank=True, verbose_name="分值")

    def __str__(self):
        return self.lei

    class Meta:
        verbose_name = '同行现货变化'
        verbose_name_plural = verbose_name


class Clouds(models.Model):
    """
    信息
    """
    lei = models.CharField(max_length=50,null=True, blank=True, verbose_name="类")
    up = models.CharField(max_length=50,null=True, blank=True, verbose_name="上限")
    down = models.CharField(max_length=50,null=True, blank=True, verbose_name="下限")
    score = models.IntegerField(max_length=50,null=True, blank=True, verbose_name="分值")

    def __str__(self):
        return self.lei

    class Meta:
        verbose_name = '云汉商城情况'
        verbose_name_plural = verbose_name