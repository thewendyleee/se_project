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
    return render(request, "order.html")


def return_car(request):
    return render(request, "return_car.html")


# 佳辰
def personal_info(request):
    return render(request, "personal_info_v2.html")


def personal_info_update(request):
    return render(request, "personal_info_v2.html")


# 賢灝
def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")
