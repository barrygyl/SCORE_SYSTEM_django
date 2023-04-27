from django.contrib import admin

from .models import Mul,Clouds,Cloudp,Search,Same_now,Ic_now,Ic_same
# Register your models here.


class mulAdmin(admin.ModelAdmin):
    list_display = ["id", "lei", "up", "down", "score"] #显示的特征


class cloudsAdmin(admin.ModelAdmin):
    list_display = ["id", "lei", "up", "down", "score"] #显示的特征


class cloudpAdmin(admin.ModelAdmin):
    list_display = ["id", "lei", "up", "down", "score"] #显示的特征


class searchAdmin(admin.ModelAdmin):
    list_display = ["id", "lei", "up", "down", "score"] #显示的特征


class ic_sameAdmin(admin.ModelAdmin):
    list_display = ["id", "lei", "up", "down", "score"] #显示的特征


class ic_nowAdmin(admin.ModelAdmin):
    list_display = ["id", "lei", "up", "down", "score"] #显示的特征


class same_nowAdmin(admin.ModelAdmin):
    list_display = ["id", "lei", "up", "down", "score"] #显示的特征


admin.site.register(Mul, mulAdmin)
admin.site.register(Cloudp, cloudpAdmin)
admin.site.register(Clouds, cloudsAdmin)
admin.site.register(Ic_now, ic_nowAdmin)
admin.site.register(Ic_same, ic_sameAdmin)
admin.site.register(Same_now, same_nowAdmin)
admin.site.register(Search, searchAdmin)