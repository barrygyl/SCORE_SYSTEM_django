from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from .models import UserProfile
from .forms import LoginForm,RegisterPostForm
# Create your views here.


class LogoutView(View):
    def get(self,request,*args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse("login"))


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.roles_id == 1:
                return HttpResponseRedirect(reverse("goods_list_upload"))
            elif request.user.roles_id == 2:
                return HttpResponseRedirect(reverse("goods_list_test"))
            else:
                return HttpResponseRedirect(reverse("goods_list"))
        return render(request,"login1.html")

    def post(self,request, *args, **kwargs):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data["Username"]
            password = login_form.cleaned_data["Password"]
            #通过用户密码查询用户是否存在
            user = authenticate(username=user_name, password=password)

            if user is not None:
                #查询到用户
                login(request,user)
                #登录成功后返回页面（不同角色跳转不同）
                if user.roles_id == 1:
                    return HttpResponseRedirect(reverse("goods_list_upload"))
                elif user.roles_id == 2:
                    return HttpResponseRedirect(reverse("goods_list_test"))
                else:
                    return HttpResponseRedirect(reverse("goods_list"))
            else:
                #未查询到用户
                return render(request, "login1.html", {"msg": "用户名或密码错误"})
        else:
            return render(request, "login1.html", {"login_form": login_form})


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "register.html")

    def post(self, request, *args, **kwargs):
        register_post_form = RegisterPostForm(request.POST)
        if register_post_form.is_valid():
            user_name = register_post_form.cleaned_data["Username"]
            password = register_post_form.cleaned_data["Password"]
            mobile = register_post_form.cleaned_data["Mobile"]
            name = register_post_form.cleaned_data["Nick_name"]
            # 通过用户名查询用户是否存在
            user = UserProfile(username=user_name)
            user.set_password(password)
            user.mobile = mobile
            user.name = name
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse("goods_list"))
        else:
                # 查询到用户
                return render(request, "login1.html", {"msg": "注册信息输入错误"})