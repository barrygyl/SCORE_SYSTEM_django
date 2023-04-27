"""ScoreSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.static import serve
from django.urls import path, include,register_converter,re_path
from django.views.generic import TemplateView

from system.views import LoginView, LogoutView, RegisterView
from goods.views import Goods_testView,gradS,gradu,gradf,editxS,getpassS,depassS,editxu, eidtxf, export_users_xls, getpassfu, depassfu, upsort,depassf,  tesort,getpassf, Goods_uploadView,filter3, upload_delete,upload_edit,upload_edit_back, search11, filter11, search1, filter1, uploadView, search, filter, getpass, depass, grad, GoodsView, editx
from .settings import MEDIA_ROOT


from django.contrib.staticfiles.views import serve
from django.urls import re_path

def return_static(request, path, insecure=True, **kwargs):
  return serve(request, path, insecure, **kwargs)


urlpatterns = [
    re_path(r'^static/(?P<path>.*)$', return_static, name='static'), # 添加这行

    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name = "login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    #删除
    path('upload_delete/', upload_delete, name="upload_delete"),
    #编辑
    path('upload_edit/', upload_edit, name="upload_edit"),
    path('upload_edit_back/', upload_edit_back, name="upload_edit_back"),
    path('editx/', editx, name="editx"),
    path('editxu/', editxu, name="editxu"),
    path('eidtxf/', eidtxf, name="editxf"),
    path('eidtxS/', editxS, name="editxS"),
    #审批
    path('getpass/', getpass, name="getpass"),
    path('depass/', depass, name="depass"),
    path('getpassf/', getpassf, name="getpassf"),
    path('depassf/', depassf, name="depassf"),
    path('getpassfu/', getpassfu, name="getpassfu"),
    path('depassfu/', depassfu, name="depassfu"),
    path('getpassS/', getpassS, name="getpassS"),
    path('depassS/', depassS, name="depassS"),
    #评级
    path('grad/', grad, name="grad"),
    path('gradS/', gradS, name="gradS"),
    path('gradf/', gradf, name="gradf"),
    path('gradu/', gradu, name="gradu"),
    #筛选搜索排序
    path('search/', search, name="search"),
    path('filter/', filter, name="filter"),
    path('search1/', search1, name="search1"),
    path('filter1/', filter1, name="filter1"),
    path('filter3/', filter3, name="filter3"),
    path('search11/', search11, name="search11"),
    path('filter11/', filter11, name="filter11"),
    path('upsort/', upsort, name="upsort"),
    path('tesort/', tesort, name="tesort"),
    # 配置上传文件
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    path('upload/', uploadView.as_view(), name="upload"),
    #导出
    path(r'^export/xls/$', export_users_xls, name='export_users_xls'),
    #物料url
    path('Goods_testView/', Goods_testView.as_view(), name="goods_list_test"),
    path('Goods_uploadView/', Goods_uploadView.as_view(), name="goods_list_upload"),
    path('GoodsView/', GoodsView.as_view(), name="goods_list"),
]
