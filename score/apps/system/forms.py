# 人工智能
# 项目：ScoreSystem
# 开发人：高云龙
# 开发时间：2022/10/19  15:16
# 开发工具：PyCharm
from django import forms
from .models import UserProfile


class LoginForm(forms.Form):
    Username = forms.CharField(required=True, error_messages={"required": "请填写用户名"})
    Password = forms.CharField(required=True, error_messages={"required": "请填写密码"})


class RegisterPostForm(forms.Form):
    Username = forms.CharField(required=True, min_length=2)
    Password = forms.CharField(required=True, min_length=3)
    Nick_name = forms.CharField(required=True,max_length=11,error_messages={'required': u'名字最长为4'})
    Mobile = forms.CharField(required=True,max_length=11,min_length=11,error_messages={'required': u'请输入正确的电话号码'})

    def clean_username(self):
        Username = self.data.get("Username")
        users = UserProfile.objects.filter(Username=Username)
        if users:
            raise forms.ValidationError("用户已存在")
        return Username