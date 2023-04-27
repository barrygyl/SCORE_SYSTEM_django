from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from datetime import datetime
import xlwt
import time

from .models import Goods
from system.models import UserProfile
from edit.models import Mul, Search, Cloudp, Ic_now, Ic_same, Clouds, Same_now


# Create your views here.
class Goods_uploadView(View):

    def get(self,request,*args, **kwargs):
        #从数据库获取数据
        all_goods = Goods.objects.all()
        goods_nums = Goods.objects.count()
        all_users = UserProfile.objects.all()
        return render(request, "goods_list_upload.html", {
            "all_goods": all_goods,
            "goods_nums": goods_nums,
            "all_users":all_users
            })


class GoodsView(View):

    def get(self,request,*args, **kwargs):
        #从数据库获取数据
        all_goods = Goods.objects.all()
        goods_nums = Goods.objects.count()
        all_users = UserProfile.objects.all()
        return render(request, "goods_list.html", {
            "all_goods": all_goods,
            "goods_nums": goods_nums,
            "all_users":all_users
            })


class Goods_testView(View):

    def get(self, request):
        all_goods = Goods.objects.all()
        goods_nums = Goods.objects.count()
        all_users = UserProfile.objects.all()
        goods_pass = Goods.objects.filter(state="通过")
        goods_pass = goods_pass.count()
        shaixuan = 0
        paixu = 0

        return render(request, "goods_list_test.html", {
            "all_goods": all_goods,
            "goods_nums": goods_nums,
            "all_users":all_users,
            "goods_pass":goods_pass,
            "shaixuan":shaixuan,
            'paixu':paixu
            })


class uploadView(View):

    def post(self, request, *args, **kwargs):
        version = request.POST.get('version')
        x1 = request.POST.get('x1')
        x2 = request.POST.get('x2')
        goods = Goods.objects.filter(version=version)
        if goods:
            return HttpResponse("该物料已存在。")

        else:
            cost = request.POST.get('cost')
            rp = request.POST.get('rp')
            if cost != None and rp != None:
                mul = float(rp) / float(cost)
            else:
                mul = None
            search = request.POST.get('search')
            cloudp = request.POST.get('cloudp')
            ic_same = request.POST.get('ic_same')
            ic_now = request.POST.get('ic_now')
            same_now = request.POST.get('same_now')
            clouds = request.POST.get('clouds')
            total = totle_cu(int(mul), int(search), int(cloudp), int(ic_same),
                                   int(ic_now), int(same_now), int(clouds))
            detail = request.POST.get('detail')
            user = request.user.name
            mul = format(mul, '.2f')
            a = datetime.now()
            b = a.strftime("%Y-%m-%d")
            add_time = b
            Goods.objects.get_or_create(version=version, x1=x1, x2=x2, cost=cost, rp=rp, mul=mul, search=search, clouds=clouds, cloudp=cloudp,
                                        ic_now=ic_now, ic_same=ic_same, same_now=same_now, user=user, detail=detail, total=total,
                                        add_time=add_time)
            return HttpResponseRedirect(reverse("goods_list_upload"))




def upload_delete(request):
    id = request.GET.get('id')
    goods = Goods.objects.get(id=id)
    if goods.state == "不通过" or goods.state == "审核中":
        if request.user.name == goods.user:
            goods.delete()
            return HttpResponseRedirect(reverse("goods_list_upload"))
        else:
            return HttpResponse("你没有操作的权限。")
    else:
        return HttpResponse("你没有删除的权限。")


def getpass(request):
    id = request.GET.get('id')
    chor = request.GET.get('chor')
    goods = Goods.objects.get(id=id)
    goods.state = "通过"
    goods.save()
    all_goods = Goods.objects.all()
    goods_nums = Goods.objects.count()
    all_users = UserProfile.objects.all()
    goods_pass = Goods.objects.filter(state="通过")
    goods_pass = goods_pass.count()
    shaixuan = 0
    chor1 = int(chor)

    return render(request, "goods_list_test.html", {
        "all_goods": all_goods,
        "goods_nums": goods_nums,
        "all_users": all_users,
        "goods_pass": goods_pass,
        "shaixuan": shaixuan,
        'chor':chor,
        'chor1':chor1
    })


def depass(request):
    id = request.GET.get('id')

    goods = Goods.objects.get(id=id)
    goods.state = "不通过"
    goods.save()
    all_goods = Goods.objects.all()
    goods_nums = Goods.objects.count()
    all_users = UserProfile.objects.all()
    goods_pass = Goods.objects.filter(state="通过")
    goods_pass = goods_pass.count()
    shaixuan = 0
    chor = request.GET.get('chor')
    chor1 = int(chor)

    return render(request, "goods_list_test.html", {
        "all_goods": all_goods,
        "goods_nums": goods_nums,
        "all_users": all_users,
        "goods_pass": goods_pass,
        "shaixuan": shaixuan,
        'chor':chor,
        'chor1':chor1
    })


def getpassf(request):
    id = request.GET.get('id')
    goods = Goods.objects.get(id=id)
    if goods.state == '通过' or goods.state =='不通过':
        goods.state = "通过"
        goods.save()
        goods1 = Goods.objects.filter(state='通过')
        goods2 = Goods.objects.filter(state='不通过')
        goods = goods1 | goods2
        goods_nums = goods.count()
        all_users = UserProfile.objects.all()
        goods_pass = goods.filter(state="通过")
        goods_pass = goods_pass.count()
        chor = request.GET.get('chor')
        chor1 = int(chor)
        shaixuan = 1
        usersf = '已审核'
        return render(request, "goods_list_test.html", {
            "all_goods": goods,
            "goods_nums": goods_nums,
            "all_users": all_users,
            "shaixuan": shaixuan,
            "goods_pass":goods_pass,
            'usersf':usersf,
            'chor':chor,
            'chor1':chor1
        })
    else:
        goods.state = "通过"
        goods.save()
        goods1 = Goods.objects.filter(state='审核中')
        goods_nums = goods1.count()
        all_users = UserProfile.objects.all()
        shaixuan = 1
        goods_pass = goods.filter(state="通过")
        goods_pass = goods_pass.count()
        usersf = '未审核'
        chor = request.GET.get('chor')
        chor1 = int(chor)
        return render(request, "goods_list_test.html", {
            "all_goods": goods1,
            "goods_nums": goods_nums,
            "all_users": all_users,
            "shaixuan": shaixuan,
            "goods_pass": goods_pass,
            'chor': chor,
            'usersf':usersf,
            'chor1': chor1
        })


def depassf(request):
    id = request.GET.get('id')
    goods = Goods.objects.get(id=id)
    if goods.state == '通过' or goods.state =='不通过':
        goods.state = "不通过"
        goods.save()
        goods1 = Goods.objects.filter(state='通过')
        goods2 = Goods.objects.filter(state='不通过')
        goods = goods1 | goods2
        goods_nums = goods.count()
        all_users = UserProfile.objects.all()
        goods_pass = goods.filter(state="通过")
        goods_pass = goods_pass.count()
        shaixuan = 1
        chor = request.GET.get('chor')
        chor1 = int(chor)
        usersf = '已审核'
        return render(request, "goods_list_test.html", {
            "all_goods": goods,
            "goods_nums": goods_nums,
            "all_users": all_users,
            "shaixuan": shaixuan,
            "goods_pass":goods_pass,
            'usersf':usersf,
            'chor':chor,
            'chor1':chor1
        })
    else:
        goods.state = "不通过"
        goods.save()
        goods1 = Goods.objects.filter(state='审核中')
        goods_nums = goods1.count()
        all_users = UserProfile.objects.all()
        goods_pass = 0
        shaixuan = 1
        usersf = '未审核'
        chor = request.GET.get('chor')
        chor1 = int(chor)
        return render(request, "goods_list_test.html", {
            "all_goods": goods1,
            "goods_nums": goods_nums,
            "all_users": all_users,
            "shaixuan": shaixuan,
            "goods_pass": goods_pass,
            'chor': chor,
            'usersf':usersf,
            'chor1': chor1
        })


def eidtxf(request):
    id = request.GET.get('id')
    goods = Goods.objects.get(id=id)
    if goods.state == '通过' or goods.state =='不通过':
        goods.x1 = request.POST.get('x1')
        goods.x2 = request.POST.get('x2')
        goods.save()
        goods1 = Goods.objects.filter(state='通过')
        goods2 = Goods.objects.filter(state='不通过')
        goods = goods1 | goods2
        goods_nums = goods.count()
        all_users = UserProfile.objects.all()
        goods_pass = goods.filter(state="通过")
        goods_pass = goods_pass.count()
        chor = request.GET.get('id')
        chor1 = int(chor)
        shaixuan = 1
        paixu = 0
        usersf = '已审核'
        return render(request, "goods_list_test.html", {
            "all_goods": goods,
            "goods_nums": goods_nums,
            "all_users": all_users,
            "shaixuan": shaixuan,
            "goods_pass":goods_pass,
            'usersf':usersf,
            'chor':chor,
            'chor1':chor1,
            'paixu':paixu
        })
    else:
        goods.x1 = request.POST.get('x1')
        goods.x2 = request.POST.get('x2')
        goods.save()
        goods1 = Goods.objects.filter(state='审核中')
        goods_nums = goods1.count()
        all_users = UserProfile.objects.all()
        shaixuan = 1
        goods_pass = goods.filter(state="通过")
        goods_pass = goods_pass.count()
        usersf = '未审核'
        chor = request.GET.get('id')
        chor1 = int(chor)
        paixu = 0
        return render(request, "goods_list_test.html", {
            "all_goods": goods1,
            "goods_nums": goods_nums,
            "all_users": all_users,
            "shaixuan": shaixuan,
            "goods_pass": goods_pass,
            'chor': chor,
            'usersf':usersf,
            'chor1': chor1,
            'paixu':paixu
        })


def editxu(request):
    id = request.GET.get('id')
    goods = Goods.objects.get(id=id)
    goods.x1 = request.POST.get('x1')
    goods.x2 = request.POST.get('x2')
    goods.save()
    user = goods.user
    goods1 = Goods.objects.filter(user=user)
    goods_nums = goods1.count()
    all_users = UserProfile.objects.all()
    goods_pass = goods1.filter(state="通过")
    goods_pass = goods_pass.count()
    shaixuan = 2
    paixu = 0
    chor = request.GET.get('id')
    chor1 = int(chor)
    return render(request, "goods_list_test.html", {
        "all_goods": goods1,
        "goods_nums": goods_nums,
        "all_users": all_users,
        "goods_pass": goods_pass,
        "shaixuan": shaixuan,
        'chor': chor,
        'chor1': chor1,
        'paixu':paixu
    })


def grad(request):
    id = request.GET.get('id')
    goods = Goods.objects.get(id=id)
    goods.grade = request.POST.get('grade')
    goods.save()
    return HttpResponseRedirect(reverse("goods_list_test"))


def gradS(request):
    id = request.GET.get('id')
    goods = Goods.objects.get(id=id)
    goods.grade = request.POST.get('grade')
    goods.save()
    goods = Goods.objects.all().order_by('-total')
    goods_nums = goods.count()
    all_users = UserProfile.objects.all()
    goods_pass = goods.filter(state="通过")
    goods_pass = goods_pass.count()
    shaixuan = 0
    paixu = 1
    chor = request.GET.get('id')
    chor1 = chor
    return render(request, "goods_list_test.html", {
        "all_goods": goods,
        "goods_nums": goods_nums,
        "all_users": all_users,
        "goods_pass": goods_pass,
        "shaixuan": shaixuan,
        'chor': chor,
        'chor1': chor1,
        'paixu': paixu
    })


def gradu(request):
    id = request.GET.get('id')
    goods = Goods.objects.get(id=id)
    goods.grade = request.POST.get('grade')
    goods.save()
    user = goods.user
    goods1 = Goods.objects.filter(user=user)
    goods_nums = goods1.count()
    all_users = UserProfile.objects.all()
    goods_pass = goods1.filter(state="通过")
    goods_pass = goods_pass.count()
    shaixuan = 2
    paixu = 0
    chor = request.GET.get('id')
    chor1 = int(chor)
    return render(request, "goods_list_test.html", {
        "all_goods": goods1,
        "goods_nums": goods_nums,
        "all_users": all_users,
        "goods_pass": goods_pass,
        "shaixuan": shaixuan,
        'chor': chor,
        'chor1': chor1,
        'paixu':paixu
    })


def gradf(request):
    id = request.GET.get('id')
    goods = Goods.objects.get(id=id)
    goods.grade = request.POST.get('grade')
    goods.save()
    if goods.state == '通过' or goods.state =='不通过':
        goods1 = Goods.objects.filter(state='通过')
        goods2 = Goods.objects.filter(state='不通过')
        goods = goods1 | goods2
        goods_nums = goods.count()
        all_users = UserProfile.objects.all()
        goods_pass = goods.filter(state="通过")
        goods_pass = goods_pass.count()
        chor = request.GET.get('id')
        chor1 = int(chor)
        shaixuan = 1
        paixu = 0
        usersf = '已审核'
        return render(request, "goods_list_test.html", {
            "all_goods": goods,
            "goods_nums": goods_nums,
            "all_users": all_users,
            "shaixuan": shaixuan,
            "goods_pass":goods_pass,
            'usersf':usersf,
            'chor':chor,
            'chor1':chor1,
            'paixu':paixu
        })
    else:
        goods1 = Goods.objects.filter(state='审核中')
        goods_nums = goods1.count()
        all_users = UserProfile.objects.all()
        shaixuan = 1
        goods_pass = goods.filter(state="通过")
        goods_pass = goods_pass.count()
        usersf = '未审核'
        chor = request.GET.get('id')
        chor1 = int(chor)
        paixu = 0
        return render(request, "goods_list_test.html", {
            "all_goods": goods1,
            "goods_nums": goods_nums,
            "all_users": all_users,
            "shaixuan": shaixuan,
            "goods_pass": goods_pass,
            'chor': chor,
            'usersf':usersf,
            'chor1': chor1,
            'paixu':paixu
        })





def editx(request):
    id = request.GET.get('id')
    goods = Goods.objects.get(id=id)
    goods.x1 = request.POST.get('x1')
    goods.x2 = request.POST.get('x2')
    goods.save()
    all_goods = Goods.objects.all()
    goods_nums = Goods.objects.count()
    all_users = UserProfile.objects.all()
    goods_pass = Goods.objects.filter(state="通过")
    goods_pass = goods_pass.count()
    shaixuan = 0
    paixu = 0
    chor = request.GET.get('id')
    chor1 = int(chor)

    return render(request, "goods_list_test.html", {
        "all_goods": all_goods,
        "goods_nums": goods_nums,
        "all_users": all_users,
        "goods_pass": goods_pass,
        "shaixuan": shaixuan,
        'chor':chor,
        'chor1':chor1,
        'paixu':paixu
    })


def upload_edit(request):
    id = request.GET.get('id')
    goods = Goods.objects.get(id=id)
    if goods.state == "不通过" or goods.state == "审核中":
        if request.user.name == goods.user:
            return render(request, "goods_edit_upload.html", {
                "goods": goods,
            })
        else:
            return HttpResponse("你没有操作的权限。")
    else:
        return HttpResponse("你没有操作的权限。")


def score(A,totle,b):
    try:
        for a in A.objects.all():
            if b>= a.down and b<a.up:
                totle += a.score
    except:
            totle +=a.score
    return totle

def totle_cu(a,b,c,d,e,f,g):
    totle = 0
    if a == None:
        totle += 15
    else:
        for mul in Mul.objects.all():
            try:
                if a>= int(mul.down) and a<int(mul.up):
                    totle += mul.score
                    break
            except:
                if a >= int(mul.down):
                    totle += mul.score
                    break
    """
    scorelist = [Search, Cloudp, Ic_same, Ic_now, Same_now, Clouds]
    culist =[b, c, d, e, f, g]
    i = 0
    for sl in scorelist:
        cl = culist[i]
        try:
            for ex in sl.objects.all():
                if cl >= ex.down and cl < ex.up:
                    totle += ex.score
        except:
            totle += ex.score
        i +=1
    return totle
"""
    for search in Search.objects.all():
        try:
            if b>= int(search.down) and b<int(search.up):
                totle += search.score
                break
        except:
            if b>= int(search.down):
                totle +=search.score
                break
    for cloudp in Cloudp.objects.all():
        try:
            if c>= int(cloudp.down) and c<int(cloudp.up):
                totle += cloudp.score
                break
        except:
            if c>= int(cloudp.down):
                totle +=cloudp.score
                break
    for ic_same in Ic_same.objects.all():
        try:
            if d>= int(ic_same.down) and d<int(ic_same.up):
                totle += ic_same.score
                break
        except:
            if d>= int(ic_same.down):
                totle +=ic_same.score
                break
    for ic_now in Ic_now.objects.all():
        try:
            if e>= float(ic_now.down) and e<float(ic_now.up):
                totle += ic_now.score
                break
        except:
            if e>= float(ic_now.down):
                totle +=ic_now.score
                break
    for same_now in Same_now.objects.all():
        try:
            if f>= int(same_now.down) and f<int(same_now.up):
                totle += same_now.score
                break
        except:
            if f>= int(same_now.down):
                totle +=same_now.score
                break
    for clouds in Clouds.objects.all():
        try:
            if g>= int(clouds.down) and g<int(clouds.up):
                totle += clouds.score
                break
        except:
            if g>= int(clouds.down):
                totle +=clouds.score
                break
    return totle

def upload_edit_back(request):
    id = request.GET.get('id')
    goods = Goods.objects.get(id=id)
    goods.version = request.POST.get('version')
    goods.x1 = request.POST.get('x1')
    goods.x2 = request.POST.get('x2')
    goods.cost = request.POST.get('cost')
    goods.rp = request.POST.get('rp')
    if goods.cost != None and goods.rp != None:
         goods.mul = int(goods.rp)/int(goods.cost)
    else:
        goods.mul = None

    goods.search = request.POST.get('search')
    goods.cloudp = request.POST.get('cloudp')
    goods.ic_same = request.POST.get('ic_same')
    goods.ic_now = request.POST.get('ic_now')
    goods.same_now = request.POST.get('same_now')
    goods.clouds = request.POST.get('clouds')
    goods.total = totle_cu(int(goods.mul),int(goods.search),int(goods.cloudp),int(goods.ic_same),
                           int(goods.ic_now),int(goods.same_now),int(goods.clouds))
    goods.detail = request.POST.get('detail')
    goods.mul = format(goods.mul, '.2f')
    goods.state = "审核中"
    goods.save()
    return HttpResponseRedirect(reverse("goods_list_upload"))

def filter(request):
    user = request.POST.get('user')
    if user =="所有":
        return HttpResponseRedirect(reverse("goods_list_upload"))
    else:
        goods = Goods.objects.filter(user=user)
        goods_nums = goods.count()
        all_users = UserProfile.objects.all()
        return render(request, "goods_list_upload.html", {
            "all_goods": goods,
            "goods_nums": goods_nums,
            "all_users":all_users
            })


def upsort(request):
        goods = Goods.objects.all().order_by('-total')
        goods_nums = goods.count()
        all_users = UserProfile.objects.all()
        return render(request, "goods_list_upload.html", {
            "all_goods": goods,
            "goods_nums": goods_nums,
            "all_users":all_users
            })


def tesort(request):
    goods = Goods.objects.all().order_by('-total')
    goods_nums = goods.count()
    all_users = UserProfile.objects.all()
    goods_pass = goods.filter(state="通过")
    goods_pass = goods_pass.count()
    shaixuan = 0
    paixu = 1
    return render(request, "goods_list_test.html", {
        "all_goods": goods,
        "goods_nums": goods_nums,
        "all_users": all_users,
        "goods_pass": goods_pass,
        'shaixuan':shaixuan,
        'paixu':paixu
    })


def getpassS(request):
    id = request.GET.get('id')
    goods = Goods.objects.get(id=id)
    goods.state = "通过"
    goods.save()
    goods = Goods.objects.all().order_by('-total')
    goods_nums = goods.count()
    all_users = UserProfile.objects.all()
    goods_pass = goods.filter(state="通过")
    goods_pass = goods_pass.count()
    shaixuan = 0
    paixu = 1
    chor = request.GET.get('chor')
    chor1 = int(chor)
    return render(request, "goods_list_test.html", {
        "all_goods": goods,
        "goods_nums": goods_nums,
        "all_users":all_users,
        "goods_pass":goods_pass,
        "shaixuan": shaixuan,
        'chor': chor,
        'chor1': chor1,
        'paixu':paixu
        })


def depassS(request):
    id = request.GET.get('id')
    goods = Goods.objects.get(id=id)
    goods.state = "不通过"
    goods.save()
    goods = Goods.objects.all().order_by('-total')
    goods_nums = goods.count()
    all_users = UserProfile.objects.all()
    goods_pass = goods.filter(state="通过")
    goods_pass = goods_pass.count()
    shaixuan = 0
    paixu = 1
    chor = request.GET.get('chor')
    chor1 = int(chor)
    return render(request, "goods_list_test.html", {
        "all_goods": goods,
        "goods_nums": goods_nums,
        "all_users":all_users,
        "goods_pass":goods_pass,
        "shaixuan": shaixuan,
        'chor': chor,
        'chor1': chor1,
        'paixu':paixu
        })


def editxS(request):
    id = request.GET.get('id')
    goods = Goods.objects.get(id=id)
    goods.x1 = request.POST.get('x1')
    goods.x2 = request.POST.get('x2')
    goods.save()
    goods = Goods.objects.all().order_by('-total')
    goods_nums = goods.count()
    all_users = UserProfile.objects.all()
    goods_pass = goods.filter(state="通过")
    goods_pass = goods_pass.count()
    shaixuan = 0
    paixu = 1
    chor = request.GET.get('chor')
    chor1 = int(chor)
    return render(request, "goods_list_test.html", {
        "all_goods": goods,
        "goods_nums": goods_nums,
        "all_users":all_users,
        "goods_pass":goods_pass,
        "shaixuan": shaixuan,
        'chor': chor,
        'chor1': chor1,
        'paixu':paixu
        })

def filter1(request):
    user = request.POST.get('user')
    if user =="所有":
        return HttpResponseRedirect(reverse("goods_list_test"))
    else:
        goods = Goods.objects.filter(user=user)
        goods_nums = goods.count()
        all_users = UserProfile.objects.all()
        goods_pass = goods.filter(state="通过")
        goods_pass = goods_pass.count()
        shaixuan = 2
        usersf = user
        paixu = 0
        return render(request, "goods_list_test.html", {
            "all_goods": goods,
            "goods_nums": goods_nums,
            "all_users":all_users,
            "goods_pass":goods_pass,
            "shaixuan": shaixuan,
            "usersf1": usersf,
            'paixu':paixu
            })


def getpassfu(request):
    id = request.GET.get('id')
    goods = Goods.objects.get(id=id)
    goods.state = "通过"
    goods.save()
    user = goods.user
    goods1 = Goods.objects.filter(user=user)
    goods_nums = goods1.count()
    all_users = UserProfile.objects.all()
    goods_pass = goods1.filter(state="通过")
    goods_pass = goods_pass.count()
    shaixuan = 2
    chor = request.GET.get('chor')
    chor1 = int(chor)
    paixu = 0
    return render(request, "goods_list_test.html", {
        "all_goods": goods1,
        "goods_nums": goods_nums,
        "all_users":all_users,
        "goods_pass":goods_pass,
        "shaixuan": shaixuan,
        'chor': chor,
        'chor1': chor1,
        'paixu':paixu
        })


def depassfu(request):
    id = request.GET.get('id')
    goods = Goods.objects.get(id=id)
    goods.state = "不通过"
    goods.save()
    user = goods.user
    goods1 = Goods.objects.filter(user=user)
    goods_nums = goods1.count()
    all_users = UserProfile.objects.all()
    goods_pass = goods1.filter(state="通过")
    goods_pass = goods_pass.count()
    shaixuan = 2
    paixu = 0
    chor = request.GET.get('chor')
    chor1 = int(chor)
    return render(request, "goods_list_test.html", {
        "all_goods": goods1,
        "goods_nums": goods_nums,
        "all_users":all_users,
        "goods_pass":goods_pass,
        "shaixuan": shaixuan,
        'chor': chor,
        'chor1': chor1,
        'paixu':paixu
        })



def filter11(request):
    user = request.POST.get('user')
    if user =="所有":
        return HttpResponseRedirect(reverse("goods_list"))
    else:
        goods = Goods.objects.filter(user=user)
        goods_nums = goods.count()
        all_users = UserProfile.objects.all()
        paixu = 0
        shaixuan = 2
        goods_pass = goods.filter(state="通过")
        goods_pass = goods_pass.count()
        return render(request, "goods_list.html", {
            "all_goods": goods,
            "goods_nums": goods_nums,
            "all_users":all_users,
            "shaixuan": shaixuan,
            "goods_pass":goods_pass,
            'paixu':paixu
            })


def filter3(request):
    user = request.POST.get('state')
    if user =="所有":
        return HttpResponseRedirect(reverse("goods_list_test"))
    else:
        if user == "已审核":
            goods = Goods.objects.filter(state='通过')
            goods1 = Goods.objects.filter(state='不通过')
            goods = goods1 | goods
            goods_nums = goods.count()
            all_users = UserProfile.objects.all()
            shaixuan = 1
            paixu = 0
            goods_pass = goods.filter(state="通过")
            goods_pass = goods_pass.count()
            usersf = user
            return render(request, "goods_list_test.html", {
                "all_goods": goods,
                "goods_nums": goods_nums,
                "all_users":all_users,
                "shaixuan":shaixuan,
                "goods_pass":goods_pass,
                "usersf": usersf,
                'paixu':paixu
                })
        else:
            goods = Goods.objects.filter(state='审核中')
            goods_nums = goods.count()
            all_users = UserProfile.objects.all()
            paixu = 0
            shaixuan = 1
            goods_pass =0
            usersf = user
            return render(request, "goods_list_test.html", {
                "all_goods": goods,
                "goods_nums": goods_nums,
                "all_users":all_users,
                "shaixuan": shaixuan,
                "usersf": usersf,
                "goods_pass": goods_pass,
                'paixu':paixu
                })


def search(request):
    vision = request.POST.get('search')
    if vision =="":
        return HttpResponseRedirect(reverse("goods_list_upload"))
    else:
        goods = Goods.objects.filter(version=vision)
        goods_nums = goods.count()
        all_users = UserProfile.objects.all()
        goods_pass = goods.filter(state="通过")
        goods_pass = goods_pass.count()
        paixu = 0
        shaixuan = 0
        return render(request, "goods_list_test.html", {
            "all_goods": goods,
            "goods_nums": goods_nums,
            "all_users": all_users,
            "goods_pass": goods_pass,
            'shaixuan': shaixuan,
            'paixu':paixu
        })


def search1(request):
    vision = request.POST.get('search')
    if vision =="":
        return HttpResponseRedirect(reverse("goods_list_test"))
    else:
        goods = Goods.objects.filter(version=vision)
        goods_nums = goods.count()
        all_users = UserProfile.objects.all()
        goods_pass = goods.filter(state="通过")
        goods_pass = goods_pass.count()
        paixu = 0
        shaixuan = 0
        return render(request, "goods_list_test.html", {
            "all_goods": goods,
            "goods_nums": goods_nums,
            "all_users": all_users,
            "goods_pass": goods_pass,
            'shaixuan': shaixuan,
            'paixu':paixu
        })


def search11(request):
    vision = request.POST.get('search')
    if vision =="":
        return HttpResponseRedirect(reverse("goods_list"))
    else:
        goods = Goods.objects.filter(version=vision)
        goods_nums = goods.count()
        all_users = UserProfile.objects.all()
        shaixuan = 0
        paixu = 0
        return render(request, "goods_list.html", {
            "all_goods": goods,
            "goods_nums": goods_nums,
            "all_users":all_users,
            'shaixuan':shaixuan,
            'paixu':paixu
            })


def len_byte(value):
        length = len(value)
        utf8_length = len(value.encode('utf-8'))
        length = (utf8_length - length) / 2 + length
        return int(length)


def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Goods')
    # 设置字体
    font = xlwt.Font()
    font.bold = True
    # 设置边框
    borders = xlwt.Borders()
    borders.left = xlwt.Borders.THIN
    borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN
    # 设置居中
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平方向
    alignment.vert = xlwt.Alignment.VERT_TOP  # 垂直方向
    # 定义不同的excel style
    style1 = xlwt.XFStyle()
    style1.font = font
    style1.borders = borders
    style1.alignment = alignment
    style2 = xlwt.XFStyle()
    style2.borders = borders
    style2.alignment = alignment
    style3 = xlwt.XFStyle()
    style3.borders = borders
    style3.alignment = alignment
    style4 = xlwt.XFStyle()
    style4.borders = borders
    style4.alignment = alignment
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('My goods')

    # 获取字符串长度，一个中文的长度为2

    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['型号', '添加时间', '小型包装型号', '小型包装型号2', '成本','参考价', '倍数','正能量搜索次数','云价格次数','IC网现货排名商家','IC网现货数','同行现货变化','云汉商城情况','评估人','备注','总分','物料状态','物料评级']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], style=style1)
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    rows = Goods.objects.all().values_list('version', 'add_time', 'x1', 'x2', 'cost','rp', 'mul','search','cloudp','ic_same','ic_now','same_now','clouds','user','detail','total','state','grade')
    col_width = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for row in rows:
        row = list(row)
        # 确定栏位宽度
        for j in range(len(row)):
            if col_width[j] < len_byte(str(row[j])):
                col_width[j] = len_byte(str(row[j]))

    # 设置栏位宽度，栏位宽度小于10时候采用默认宽度
    for i in range(len(col_width)):
        if col_width[i] > 10:
            ws.col(i).width = 256 * (col_width[i] + 1)
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], style=style1)

    wb.save(response)
    return response