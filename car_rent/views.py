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


#def register(request):
#    return render(request, "register.html")

def register(request):
    try:
        useid = request.GET['userid']
        account = request.GET['account']
        pwd = request.GET['pwd']
        date = request.GET['date']
        phone = request.GET['phone']
        address = request.GET['address']
        inputsex = request.GET['input_sex']
    except:
        useid =None
    if useid != None:
        items = User.objects.create( user_name=useid, account=account, password=pwd,telephone=phone, address=address
                                ,birthday=date, sex=inputsex)
        items.save()
    return render(request, "register.html")



def UserManager(request):
    user = {}
    # 需要設置綁定登入者的機制 #############
    entry = User.objects.get(id=1)
    user['account'] = entry.account
    user['password'] = entry.password
    user['name'] = entry.user_name
    user['gender'] = entry.sex
    user['birth'] = entry.birthday
    user['address'] = entry.address
    user['tel_number'] = entry.telephone
    
    return render(request , "personal_info_v2.html", user)

def UserUpdateManager(request):
    user = {}
    entry = User.objects.get(id=1)
    user['account'] = entry.account
    user['password'] = entry.password
    user['name'] = entry.user_name
    user['gender'] = entry.sex
    user['birth'] = entry.birthday
    user['address'] = entry.address
    user['tel_number'] = entry.telephone
    
    return render(request , "personal_info_update_v2.html", user)

def OrderManager(request):
    order = {}
    entry = Order.objects.get(id=1)
    order['Code'] = entry.unlock_code
    order['activeT'] = entry.order_time
    order['Place'] = entry.order_station
    order['CarN'] = entry.order_car
    order['state'] = entry.order_status
    
    return render(request , "order.html", order)

def TransactionManager(request):
    transaction = {}
    data = []
    entry = Transaction.objects.all()
    # entry 需要加上搜尋指定資料的機制 ##############

    for i in range(len(list(entry))):
        data.append(str(list(entry)[i].transaction_id))  

    transaction['trans_ID'] = data

    return render(request , "transaction.html", transaction)

def TransDetailManager(request):
    transdetail = {}
    # entry_Order = Order.objects.get(id=1) #transaction 缺乏id 目前占用order id
    # entry = Transaction.objects.filter() #這裡id應該要跟著前一頁選擇的id 而定
    # entry = request[0]
    # 須想辦法從transaction.html 取得點擊的trans編號，傳給transdetailManager #############
    data = request.POST.get('12')
    # data = request.json()
    print(data,"*************")
    transdetail['trans_id'] = request
    # transdetail['get_time'] = entry.pick_up_car_time
    # transdetail['return_time'] = entry.return_car_time
    # transdetail['viechle_id'] = entry.transaction_car
    # transdetail['station'] = entry.transaction_station
    # transdetail['price'] = entry.pay

    return render(request, "transaction_detail.html", transdetail)
    
