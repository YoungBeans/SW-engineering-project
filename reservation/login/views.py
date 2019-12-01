from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.sessions.models import Session
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from reserv.models import Menu, Food

# Create your views here.

def sign_up (request) :
    if request.method == "POST" :
        userid = request.POST["id"]
        password = request.POST["pwd"]
        # city = request.POST["city"]
        # local = Location.objects.get(city=city)
        nickname = request.POST["nickname"]
        phone = request.POST["phone_number"]
        checkpwd = request.POST["checkpwd"]


        if User.objects.filter(idName=userid) :
            errMsg = "이미 존재하는 아이디입니다."
            return render(request, "login/signup.html", {"errMsg" : errMsg})

        if checkpwd != password :
            errMsg = "잘못된 패스워드를 입력했습니다."
            return redirect("home", errMsg)

        user = User (
            idName = userid,
            password = password,
            nickName = nickname,
            # location = local,
            phoneNumber = phone
        )

        user.save()
        return render(request, "login/login.html")
    else :
        return render(request, "login/signup.html")

def logout(request) :
    if request.session.get('userid') :
        request.session['userid'] = None
        request.session['manager'] = None
        return redirect("home")
    else :
        return redirect("home")

def login(request) :
    if request.method == "POST" and request.session.get('userid') == None :
        id = request.POST["id"]
        pwd = request.POST["pwd"]
#                                     컨태인을 없애 버그 픽스
        user = None
        us = User.objects.filter(idName=id, password=pwd)

        for u in us :
            user = u
        
        print(user)
        if user :
            request.session['userid'] = user.idName
            request.session['manager'] = user.isManager
            return redirect("home")
        else :
            errMsg = "로그인 실패"
            return render(request, "login/login.html", {"errMsg" : errMsg})

    elif request.session.get('userid') :
        return redirect("login")
    else :
        return render(request, "login/login.html")

def find_pwd(request) :
    if request.method == "POST" :
        username = request.POST["id"]
        phone = request.POST["number"]
        
        current_user = User.objects.filter(idName=username, phoneNumber=phone)

        if current_user :
            context = {"username" : username}
            return render(request, "login/change.html", context)
        else :
            errMsg = "cant found your id"
            return redirect("home", errMsg)
    else :
        return render(request, "login/find_pwd.html")
        
def change_pwd(request) :
    username = request.POST['id']
    pwd = request.POST['pwd']
    checkpwd = request.POST['checkpwd']

    if pwd == checkpwd :
        user = get_object_or_404(User, idName=username)
        user.password = pwd
        user.save()
        return redirect("home")
    else :
        errMsg = "please check password"
        return render(request, "login/change.html", {"errMsg" : errMsg})


def  show_review(request) :
    reviews = Review.objects.all()
    paginator = Paginator(reviews, 6)

    menu = Menu.objects.all()

    page = request.GET.get('page')
    try :
        reviews = paginator.page(page)
    except PageNotAnInteger :
        reviews = paginator.page(1)
    except EmptyPage :
        reviews = paginator.page(paginator.num_pages)
    if request.session.get("userid") :
        user = get_object_or_404(User, idName=request.session.get("userid"))
        userpk = user.pk
        context = {"reviews" : reviews, "menu" : menu, "userpk":userpk}
        return render(request, "statistics/review.html", context)
    else :
        context = {"reviews" : reviews, "menu" : menu}
        return render(request, "statistics/review.html", context)

# def test_show_review(request) :


def write_review(request) :
    menus = request.POST.get("menu")
    star = request.POST.get("star")
    title = request.POST.get("title")
    content = request.POST.get("content")
    userid = request.session.get("userid")
    user = get_object_or_404(User, idName=userid)
    # food = Food.objects.get(food=menus)
    food = get_object_or_404(Food, food=menus)
    menu = get_object_or_404(Menu, food=food)

    review = Review (
        user = user,
        title = title,
        content = content,
        menu = menu,
        star = star
    )

    review.save()

    return redirect("show_review")

def my_review(request, pk) :
    if request.session.get("userid") :

        user = get_object_or_404(User, pk=pk)

        reviews = Review.objects.filter(user = user)
        paginator = Paginator(reviews, 5)
        page = request.GET.get('page')
        try :
            reviews = paginator.page(page)
        except PageNotAnInteger :
            reviews = paginator.page(1)
        except EmptyPage :
            reviews = paginator.page(paginator.num_pages)
        
        context = {"reviews" : reviews}
        return render(request, "statistics/myreview.html", context)
    
    return redirect("home")

def modify_review(request, pk) :
    if request.method == "POST" :
        menus = request.POST.get("menu")
        star = request.POST.get("star")
        title = request.POST.get("title")
        content = request.POST.get("content")
        userid = request.session.get("userid")  
        user = get_object_or_404(User, idName=userid)
        if user :
            food = get_object_or_404(Food, food=menus)
            # food = Food.objects.get(food=menus)
            menu = get_object_or_404(Menu, food=food)

            review = get_object_or_404(Review, pk=pk)

            review.title = title
            review.content = content
            review.menu = menu
            review.star = star

            review.save()

            return redirect("my_review", pk=user.pk)
        else :
            return redirect("show_review")
    else :
        review = get_object_or_404(Review, pk=pk)

        menus = Menu.objects.all()

        context={"review" : review, "menus" : menus}
        return render(request, "statistics/modify_review.html", context)


def search_review(request) :
    if request.POST.get("menu") and request.POST.get("keyword") :
        food = request.POST.get("menu")
        keyword = request.POST.get("keyword")

        foods = get_object_or_404(Food, food=food)
        menu = get_object_or_404(Menu, food=foods)

        reviews = Review.objects.filter(menu=menu, title__icontains=keyword, content__contains=keyword)

        return render(request, "statistics/search_review.html", {"reviews" : reviews})
    elif request.POST.get("menu") :
        food = request.POST.get("menu")

        foods = get_object_or_404(Food, food=food)
        menu = get_object_or_404(Menu, food=foods)

        reviews = Review.objects.filter(menu=menu)

        return render(request, "statistics/search_review.html", {"reviews" : reviews})
    elif request.POST.get("keyword") :
        keyword = request.POST.get("keyword")

        reviews = Review.objects.filter(title__icontains=keyword, content__contains=keyword)

        return render(request, "statistics/search_review.html", {"reviews" : reviews})