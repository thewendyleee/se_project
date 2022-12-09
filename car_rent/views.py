from django.shortcuts import render

# Create your views here.

# 育慈 
def rent(request):
    return render(request, "rent.html")


def report(request):
    return render(request, "report.html")


# 欣瑩
def transaction(request):
    return render(request, "transaction.html")


def transaction_detail(request):
    return render(request, "transaction_detail.html")


# 世界
def order(request):
    inputI={'name':"查看訂單"}
    inputI['Code'] = "111423004"
    inputI['activeT'] = "2022-12-06"
    inputI['Place'] = "依仁堂"
    inputI['CarN'] = "24601"
    inputI['state'] = "尚未啟用"
    return render(request,"order.html",inputI)


def return_car(request):
    return render(request, "return_car.html")


# 佳辰
def personal_info(request):    
    context ={'age':"20"}
    context['name'] ="蘇世界"
    context['account'] ="111423004"
    context['password'] ="4125252"
    context['gender'] ="男生"
    context['address'] ="中央路11111"
    context['tel_number'] ="0977777777"
    return render(request, "personal_info_v2.html")


def personal_info_update(request):
    return render(request, "personal_info_v2.html")


# 賢灝
def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")
