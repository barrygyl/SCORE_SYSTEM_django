from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserProfile, Menu, Role
# Register your models here.


class MenuAdmin(admin.ModelAdmin):
    list_display = ["id", "name","parent", "url"] #显示的特征
    search_fields = ["name"] #搜索的字段


class RoleAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "desc"] #显示的特征
    search_fields = ["name"] #搜索的字段


class UserProfileAdmin(admin.ModelAdmin):

    list_display = ["id", "name", "username", "roles"] #显示的特征
    search_fields = ["name"] #搜索的字段

admin.site.register(Menu, MenuAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.site_header = "SCORE系统"
admin.site.site_title = "SCORE系统"
admin.site.index_title = "SCORE系统"



