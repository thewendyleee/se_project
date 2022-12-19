from django.contrib import auth, messages
from django.http import HttpResponseRedirect, JsonResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


# Create your views here.

# 育慈
def rent(request):
    user_id = request.session['user_id']
    rent_context = {}
    #查看是否有訂單
    try:
        O = Order.objects.get(order_user=user_id)
        if O!=None :
            messages.success(request, "已經有訂單")
            return redirect('/order/')
    except:
        if request.method == 'POST':
            if request.POST:
                Place = request.POST.get("place")
                CarT = request.POST.get("cartype")
        else:
            Place = None
            CarT = None

        #查看顯示剩餘車輛
        # 所有車、所有車數量
        AllCar = Car.objects.all()
        AllCarN = Car.objects.all().count()
        # 站點可使用
        bike = 0;
        motorcycle = 0;
        bikeN = 999999;
        motorcycleN = 999999;
        #從0開始
        for i in range(AllCarN):
            if (str(AllCar[i].locate_station) == Place and str(AllCar[i].status) == "正常"):
                if (str(AllCar[i].car_type) == "Bike"):
                    bikeN = i;
                    bike = bike + 1;
                if (str(AllCar[i].car_type) == "motorcycle"):
                    motorcycleN = i;
                    motorcycle = motorcycle + 1

        rent_context['num_bike'] = bike
        rent_context['num_scooter'] = motorcycle
        rent_context['user_name'] = request.session.get('user_name')

         # 預定車更新CarList
        if CarT == "腳踏車":
            if bikeN == 999999:
                messages.success(request, str(Place) + "已經沒有腳踏車了")
                return render(request, "rent.html", rent_context)
            else:
                C = AllCar[bikeN]
                C.status = '已預訂'
                C.save()
        if CarT == "電動滑板車":
            if motorcycleN == 999999:
                messages.success(request, str(Place) + "已經沒有電動滑板車了")
                return render(request, "rent.html", rent_context)
            else:
                C = AllCar[motorcycleN]
                C.status = '已預訂'
                C.save()

        #建立order物件
        if Place != None and CarT!= None:
            U = User.objects.get(id=user_id)
            S = Station.objects.get(station_name=Place)
            date1=datetime.now()
            items = Order.objects.create( order_station =S, order_time=date1,order_user =U,order_car=C)
            items.save()
            messages.success(request, "預約成功")
            return redirect('/order/')

        return render(request, "rent.html", rent_context)


def report(request):
    report_context = {}
    report_context['user_name'] = request.session.get('user_name')
    return render(request, "report.html", report_context)


# 欣瑩
def transaction(request):
    test_range = range(3)
    return render(request, "transaction.html", {'test_range': test_range, })


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


# def personal_info_update(request):
#     return render(request, "personal_info_update_v2.html")


# 賢灝
def login(request):
    if request.method == 'POST':
        acc = request.POST.get('account', False)
        password = request.POST.get('pwd', False)
        try:
            user_val = User.objects.filter(account=acc).values()
            if acc == user_val[0]['account'] and password == user_val[0]['password']:  # 判斷此帳號密碼是否正確
                # return HttpResponse('Welcome!~'+user_val[0]['user_name']) 測試用
                request.session['user_name'] = user_val[0]['user_name']
                request.session['user_id'] = user_val[0]['id']  # get user's id
                return redirect('/rent')
            else:
                messages.success(request, "密碼錯誤")
                return redirect('/login')
        except:
            messages.success(request, "帳號錯誤！")
            return redirect('/login')
    else:
        return render(request, 'login.html')


def logout(request):
    request.session.flush()
    messages.success(request, "登出成功！")
    return redirect('/login')


# def register(request):
#    return render(request, "register.html")

def register(request):
    if request.method == 'POST':
        if request.POST:
            useid = request.POST.get('userid')
            account = request.POST.get('account')
            pwd = request.POST.get('pwd')
            date = request.POST.get('date')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            inputsex = request.POST.get('input_sex')
    else:
        useid = None
    if useid != None:
        items = User.objects.create(user_name=useid, account=account, password=pwd, telephone=phone, address=address,
                                    birthday=date, sex=inputsex)
        items.save()
        return redirect('/login/')
    return render(request, "register.html")


def register_check(request):
    res = {"code": 2000, "msg": ""}
    acc = request.GET.get("account")
    if acc:
        user = User.objects.filter(account=acc).first()
        if user:
            res = {"code": 2000, "msg": "此帳號已存在"}
        # else:
        #     res = {"code": 2001, "msg": ""}
    # else:
    #     res = {"code": 2002, "msg": "请输入用户名"}
    return JsonResponse(res)


# 使用者資訊頁面呈現
def UserManager(request):
    user = {}
    user_id = request.session['user_id']
    # 綁定登入者的機制 #############
    entry = User.objects.get(id=user_id)
    user['account'] = entry.account
    user['password'] = entry.password
    user['name'] = entry.user_name
    user['gender'] = entry.sex
    user['birth'] = entry.birthday
    user['address'] = entry.address
    user['tel_number'] = entry.telephone
    user['user_name'] = request.session.get('user_name')

    return render(request, "personal_info_v2.html", user)


# 使用者剛進入修改頁面時，最初的初始值呈現
def UserUpdateManager(request):
    user = {}
    user_id = request.session['user_id']
    # 綁定登入者的機制 #############
    entry = User.objects.get(id=user_id)

    user['account'] = entry.account
    user['password'] = entry.password
    user['name'] = entry.user_name
    user['gender'] = entry.sex
    user['birth'] = entry.birthday.strftime('%Y-%m-%d')  # 日期型<input>，須接受指定格式的日期資料，不接受單純從DB回傳的datetime型別
    user['address'] = entry.address
    user['tel_number'] = entry.telephone
    user['user_name'] = request.session.get('user_name')

    # print(type(entry.birthday))  # <class 'datetime.date'> 測試用

    return render(request, "personal_info_update_v2.html", user)


# 使用者資訊修改頁面，把資料更新至資料庫，並返回至使用者資訊頁面
def UserUploadManager(request):
    user = {}
    user_id = request.session['user_id']
    # 綁定登入者的機制 #############
    entry = User.objects.get(id=user_id)

    entry.account = request.POST['account']
    entry.password = request.POST['password']
    entry.user_name = request.POST['name']
    entry.sex = request.POST['gender']
    entry.birthday = request.POST['birth']
    entry.address = request.POST['address']
    entry.telephone = request.POST['tel_number']

    entry.save()

    # --------更新完user資訊後，跳回個人資訊頁面，需重新帶入template tags------
    user['account'] = entry.account
    user['password'] = entry.password
    user['name'] = entry.user_name
    user['gender'] = entry.sex
    user['birth'] = entry.birthday
    user['address'] = entry.address
    user['tel_number'] = entry.telephone
    user['user_name'] = entry.user_name  # 導覽列上的 user_name
    print("upload work ************")

    return render(request, "personal_info_v2.html", user)


def OrderManager(request):
    user_id = request.session['user_id']
    try:
        O = Order.objects.get(order_user=user_id)
    except:
        O=None

    if O !=None:
        order = {}
        entry = Order.objects.get(order_user=user_id)
        order['Code'] = entry.unlock_code
        order['activeT'] = entry.order_time
        order['Place'] = entry.order_station
        order['CarN'] = entry.order_car
        order['state'] = entry.order_status
        order['user_name'] = request.session.get('user_name')
    else:
        entry = None
        order = {}
        order['Code'] = "無"
        order['activeT'] = "無"
        order['Place'] = "無"
        order['CarN'] = "無"
        order['state'] = "無"
        order['user_name'] = "無"
        order['user_name'] = request.session.get('user_name')
    if request.method == "POST":
        if request.POST:
            if entry!=None:
                AllCar = Car.objects.all()
                AllCarN = Car.objects.all().count()
                for i in range(AllCarN):
                    if (AllCar[i].id == entry.order_car.id):
                        C = AllCar[i]
                        C.status = '正常'
                        C.save()
                        break
                entry.delete()
    return render(request, "order.html", order)

def TransactionManager(request):
    transaction = {}
    data = []
    user_id = request.session['user_id']
    entry = Transaction.objects.filter(transaction_user=user_id)
    # entry = Transaction.objects.all()  # 測試用
    # 用登入者ID  綁定指定資料的機制 ##############

    for i in range(len(list(entry))):
        data.append(str(list(entry)[i].transaction_id))

    transaction['trans_ID'] = data
    transaction['user_name'] = request.session.get('user_name')
    return render(request, "transaction.html", transaction)


def TransDetailManager(request, trans_id):
    transdetail = {}

    entry = Transaction.objects.get(transaction_id=trans_id)
    # 用URL 綁定指定資料的機制 ##############

    transdetail['trans_id'] = entry.transaction_id
    transdetail['get_time'] = entry.pick_up_car_time
    transdetail['return_time'] = entry.return_car_time
    transdetail['vehicle_id'] = entry.transaction_car
    transdetail['station'] = entry.transaction_station
    transdetail['price'] = entry.pay
    transdetail['user_name'] = request.session.get('user_name')

    return render(request, "transaction_detail.html", transdetail)
