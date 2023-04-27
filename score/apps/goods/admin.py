from django.contrib import admin

from .models import Goods
# Register your models here.


class GoodsAdmin(admin.ModelAdmin):
    list_display = ["id", "version", "user", "total", "grade", "state"] #显示的特征
    search_fields = ["version", "user",  "grade"] #搜索的字段
    list_filter = ["version", "user",  "grade"]


admin.site.register(Goods, GoodsAdmin)