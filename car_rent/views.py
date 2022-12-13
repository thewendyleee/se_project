from django.shortcuts import render
from .models import *

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
# def order(request):
#     inputI={'name':"查看訂單"}
#     inputI['Code'] = "111423004"
#     inputI['activeT'] = "2022-12-06"
#     inputI['Place'] = "依仁堂前門"
#     inputI['CarN'] = "24601"
#     inputI['state'] = "尚未啟用"
#     return render(request,"order.html",inputI)


def return_car(request):
    return render(request, "return_car.html")


# 佳辰
# def personal_info(request):    
#     personal_info = {}
#     personal_info['account'] = 'abc123'
#     personal_info['password'] = '123456'
#     personal_info['name'] = 'Oscar'
#     personal_info['gender'] = 'Male'
#     personal_info['age'] = '24'
#     personal_info['address'] = 'Apple street'
#     personal_info['tel_number'] = '09456789'
#     return render(request, "personal_info_v2.html", personal_info)


def personal_info_update(request):
    return render(request, "personal_info_update_v2.html")


# 賢灝
def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def UserManager(request):
    user = {}
    entry = User.objects.get(id=1)
    user['account'] = entry.account
    user['password'] = entry.password
    user['name'] = entry.user_name
    user['gender'] = entry.sex
    user['birth'] = entry.birthday
    user['address'] = entry.address
    user['tel_number'] = entry.telephone
    
    return render(request , "personal_info_v2.html", user)

def OrderManager(request):
    order = {}
    entry = Order.objects.get(id=1)
    order['Code'] = entry.unlock_code
    order['activeT'] = entry.order_time
    order['Place'] = entry.order_station
    order['CarN'] = entry.order_car
    order['state'] = entry.order_status
    
    return render(request , "order.html", order)

# 缺 transaction id
def TransactionManager(request):
    transaction = {}
    transaction['test_range'] = range(Transaction.objects.count())
    entry = Order.objects.get(id=1)
    transaction['trans_ID'] = entry.unlock_code

    return render(request , "transaction.html", transaction)

def TransDetailManager(request):
    transdetail = {}
    entry_Order = Order.objects.get(id=1) #transaction 缺乏id 目前占用order id
    entry = Transaction.objects.get(id=2) #這裡id應該要跟著前一頁選擇的id 而定
    transdetail['trans_id'] = entry_Order.unlock_code
    transdetail['get_time'] = entry.pick_up_car_time
    transdetail['return_time'] = entry.return_car_time
    transdetail['viechle_id'] = entry.transaction_car
    transdetail['station'] = entry.transaction_station
    transdetail['price'] = entry.pay

    return render(request, "transaction_detail.html", transdetail)

    