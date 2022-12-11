from django.shortcuts import render

# Create your views here.

# 育慈 
def rent(request):
    num_bike = 4
    num_scooter = 5
    return render(request, "rent.html", {
        'num_bike': num_bike ,
        'num_scooter': num_scooter})


def report(request):
    return render(request, "report.html")


# 欣瑩
def transaction(request):
    test_range = range(3)
    return render(request, "transaction.html",{'test_range':test_range})


def transaction_detail(request):
    trans_detail = {}
    trans_detail['trans_id'] = '11234'
    trans_detail['get_time'] = '2022/12/44'
    trans_detail['return_time'] = '2023/2/236'
    trans_detail['viechle_id'] = '56789'
    trans_detail['station'] = '依仁堂'
    trans_detail['price'] = '100'
    return render(request, "transaction_detail.html", trans_detail)


# 世界
def order(request):
    inputI={'name':"查看訂單"}
    inputI['Code'] = "111423004"
    inputI['activeT'] = "2022-12-06"
    inputI['Place'] = "依仁堂前門"
    inputI['CarN'] = "24601"
    inputI['state'] = "尚未啟用"
    return render(request,"order.html",inputI)


def return_car(request):
    return render(request, "return_car.html")


# 佳辰
def personal_info(request):    
    personal_info = {}
    personal_info['account'] = 'abc123'
    personal_info['password'] = '123456'
    personal_info['name'] = 'Oscar'
    personal_info['gender'] = 'Male'
    personal_info['age'] = '24'
    personal_info['address'] = 'Apple street'
    personal_info['tel_number'] = '09456789'
    return render(request, "personal_info_v2.html", personal_info)


def personal_info_update(request):
    return render(request, "personal_info_update_v2.html")


# 賢灝
def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")
