from django.contrib import auth, messages
from django.http import HttpResponseRedirect, JsonResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import *
from datetime import datetime, timedelta


# Create your views here.

# 育慈
def rent(request):
    user_id = request.session['user_id']
    rent_context = {}
    data = []
    entry = Station.objects.all()
    for i in range(len(list(entry))):
        data.append(str(list(entry)[i].station_name))
    rent_context['stations'] = data
    
    
    # 查看是否有訂單
    try:
        O = Order.objects.get(order_user=user_id)
        if O != None:
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
        # 查看顯示剩餘車輛
        # 所有車、所有車數量
        AllCar = Car.objects.all()
        AllCarN = Car.objects.all().count()

        # 站點可使用
        bike = 0;
        motorcycle = 0;
        bikeN = 999999;
        motorcycleN = 999999;
        if request.method == 'POST':
            # 從0開始
            for i in range(AllCarN):
                if (str(AllCar[i].locate_station) == Place and str(AllCar[i].status) == "正常"):
                    if (str(AllCar[i].car_type) == "Bike"):
                        bikeN = i;
                        bike = bike + 1;
                    if (str(AllCar[i].car_type) == "motorcycle"):
                        motorcycleN = i;
                        motorcycle = motorcycle + 1
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
            # 建構Order物件
            if Place != None and CarT != None:
                U = User.objects.get(id=user_id)
                S = Place
                items = Order.objects.create(order_user=U, order_car=C, order_station=S)
                items.save()
                messages.success(request, "預約成功")
                return redirect('/order/')
        rent_context['Place'] = Place
        rent_context['CarT'] = CarT
        rent_context['num_bike'] = bike
        rent_context['num_scooter'] = motorcycle
        rent_context['user_name'] = request.session.get('user_name')
        return render(request, "rent.html", rent_context)


def rent_car_num_check(request):
    res = {"bike": 0, "scooter": 0}
    AllCar = Car.objects.all()
    AllCarN = Car.objects.all().count()

    if request.method == "POST":
        Place = request.POST.get("place")
        CarT = request.POST.get("cartype")
    else:
        Place = None
        CarT = None
    print(Place)
    print(CarT)
    # 計算
    bike = 0;
    motorcycle = 0;
    for i in range(AllCarN):
        if (str(AllCar[i].locate_station) == Place and str(AllCar[i].status) == "正常"):
            if (str(AllCar[i].car_type) == "Bike"):
                bike = bike + 1;
            if (str(AllCar[i].car_type) == "motorcycle"):
                motorcycle = motorcycle + 1
    res = {"bike": bike, "scooter": motorcycle}
    return JsonResponse(res)


def report(request):
    report_context = {}
    report_context['user_name'] = request.session.get('user_name')
    user_id = request.session['user_id']
    data = []
    entry = Car.objects.all()
    for i in range(len(list(entry))):
        data.append(str(list(entry)[i].id))
    report_context['cars'] = data

    if request.method == 'POST':
        if request.POST:
            Place = request.POST.get('station')
            CarId = request.POST.get('Carid')
            whatHappen = request.POST.get('happen')
        if CarId == "" or whatHappen == "":
            messages.success(request, "回報請完整填寫資訊")
        else:
            try:
                time = datetime.now()
                brokenCar = Car.objects.get(id=CarId)
                reporter = User.objects.get(id=user_id)
                newreport = Report.objects.create(report_user=reporter, report_car=brokenCar, reason=whatHappen,
                                                  date=time)
                newreport.save()
                AllCar = Car.objects.all()
                AllCarN = Car.objects.all().count()
                #判斷找尋車輛、確認目前車輛狀況
                for i in range(AllCarN):
                    if (AllCar[i].id == int(CarId)):
                        C = AllCar[i]
                        if (C.status == '維修中'):
                            messages.success(request, "已經申報")
                            break
                        else:
                            C.status = '維修中'
                            C.save()
                            messages.success(request, "申報成功")
                            break
            except:
                messages.success(request, "車輛不存在，請重新填寫")
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


def return_car(request):
    return render(request, "return_car.html")


# 賢灝
@csrf_exempt
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
    print(entry.sex=='男')
    if entry.sex =='男':
        user['s1'] = 'selected'
        user['s2'] = ''
        user['s3'] = ''
    elif entry.sex =='女':
        user['s1'] = ''
        user['s2'] = 'selected'
        user['s3'] = ''
    else:
        user['s1'] = ''
        user['s2'] = ''
        user['s3'] = 'selected'
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

    # 例外處理若未選擇gender，則提醒選擇性別，並停留至個人資訊更新頁面
    if request.POST['gender'] == "None":
        messages.success(request, "請選擇性別")
        return redirect('/personal_info_update')
    else:
        entry.sex = request.POST['gender']  # 更新gender

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
    
    #從資料庫取站
    order = {}
    data = []
    entry = Station.objects.all()
    for i in range(len(list(entry))):
        data.append(str(list(entry)[i].station_name))
    order['stations'] = data
    
    try:
        O = Order.objects.get(order_user=user_id)
    except:
        O = None

    if O != None:
        entry = Order.objects.get(order_user=user_id)
        order['Code'] = str(entry.unlock_code)[0:8]   #只取8位字母
        order['activeT'] = entry.order_use_time
        order['returnT'] = entry.order_return_time
        order['Place'] = entry.order_station
        order['CarN'] = entry.order_car
        order['state'] = entry.order_status
        order['user_name'] = request.session.get('user_name')
        if entry.order_status == '未付款':
            order['btn_text'] = "解鎖"
            order['Disable'] = False
        else:
            order['btn_text'] = "還車"
            order['Disable'] = True
    else:
        entry = None
        order = {}
        order['Code'] = "無"
        order['activeT'] = "無"
        order['returnT'] = '無'
        order['Place'] = "無"
        order['CarN'] = "無"
        order['state'] = "無"
        order['user_name'] = "無"
        order['btn_text'] = "解鎖"
        order['user_name'] = request.session.get('user_name')

    return render(request, "order.html", order)


# 處理 兩個submit button 需做出的反應
def order_upload(request):
    user_id = request.session['user_id']
    
    #從資料庫取站 
    order = {}
    data = []
    entry = Station.objects.all()
    for i in range(len(list(entry))):
        data.append(str(list(entry)[i].station_name))
    order['stations'] = data

    # 若order不存在，例外處理
    try:
        O = Order.objects.get(order_user=user_id)
    except:
        messages.success(request, "訂單不存在")
        return render(request, "rent.html")  # 例外處理，返回租車介面

    if 'unlock' in request.POST:
        if request.POST['unlock'] == '解鎖':
            #order = {}
            order['Code'] = str(O.unlock_code)[0:8]  #只取8位字母

            # 避免重新進入頁面時，用車時間被刷新
            if O.order_use_time == None:
                O.order_use_time = datetime.now()
                O.save()
                
            order['activeT'] = O.order_use_time
            order['returnT'] = ''
            order['Place'] = O.order_station
            order['CarN'] = O.order_car


            O.order_status = '使用中'
            O.save()


            order['btn_text'] = '還車'
            order['Disable'] = True
            order['state'] = O.order_status
            order['user_name'] = request.session.get('user_name')

            return render(request, "order.html", order)

        if request.POST['unlock'] == '還車':
            pick_up_time = O.order_use_time
            return_time = datetime.now()  # 還車時間
            trans_id = O.unlock_code
            trans_user = User.objects.get(id=user_id)
            # trans_car = O.order_car.id
            
            O.order_status = '已付款'
            O.save()
            
        # 處理還車站點
            station = request.POST['return_station']  # 從前端取得還車站點
            trans_station = Station.objects.get(station_name=station)  # 根據站點名稱找到Station object
            trans_station_name = trans_station.station_name  #轉為字串，用於傳入建構Transaction

            AllCar = Car.objects.all()  #所有車輛
            AllCarNum = Car.objects.all().count()  #所有車輛數
            current_car_num = 0   #目前站點車輛數

            # 計算該站點目前有多少車輛
            for i in range(AllCarNum):
                if AllCar[i].locate_station == trans_station:
                    current_car_num = current_car_num+1

            # 檢查站點車輛數是否爆滿
            if trans_station.maximum_load <= current_car_num:
                messages.success(request,'站點已爆滿，請前往其他站點停車')
                return redirect('/order')

        # 更新車輛位置，並轉為字串存入transaction
            car = O.order_car  #取得該order車輛
            car.locate_station = trans_station  # 更新車輛位置為還車之station
            car.status = '正常'
            car.save()
            trans_car = str(car.id)+"號  "+str(car.car_type.type_name) #轉為字串，用於傳入建構Transaction

        # 處理時間差算錢
            # print(str(pick_up_time)[0:19]) #測試用
            time_1 = datetime.strptime(str(pick_up_time)[0:19], '%Y-%m-%d %H:%M:%S')
            time_2 = datetime.strptime(str(return_time)[0:19], '%Y-%m-%d %H:%M:%S')
            delta = time_2 - time_1
            price = 1 + ((delta.seconds) / 60) - 480  # 因時區問題減8小時更正 ， +1表示至少一塊


        #把order轉存為transaction

            O.delete()

            transaction = Transaction.objects.create(pick_up_car_time=pick_up_time, return_car_time=return_time,
                                                     transaction_id=trans_id, transaction_user=trans_user,
                                                     transaction_car=trans_car, transaction_station=trans_station_name,
                                                     pay=price)
            transaction.save()

            return redirect('/transaction')

    if 'delete' in request.POST:
        if O != None:
            AllCar = Car.objects.all()
            AllCarN = Car.objects.all().count()
            for i in range(AllCarN):
                if (AllCar[i].id == O.order_car.id):
                    C = AllCar[i]
                    C.status = '正常'
                    C.save()
                    break
            O.delete()


        messages.success(request, "刪除成功")
        return redirect('/order')



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

    transdetail['trans_id'] = str(entry.transaction_id)[0:8]  #只取前8位
    transdetail['get_time'] = entry.pick_up_car_time
    transdetail['return_time'] = entry.return_car_time
    transdetail['vehicle_id'] = entry.transaction_car
    transdetail['station'] = entry.transaction_station
    transdetail['price'] = entry.pay
    transdetail['user_name'] = request.session.get('user_name')

    return render(request, "transaction_detail.html", transdetail)


def finishrent(request, Place, CarT):
    user_id = request.session['user_id']
    rent_context = {}
    rent_context['CarT'] = CarT
    rent_context['Place'] = Place
    rent_context['user_name'] = request.session.get('user_name')

    # 查看顯示剩餘車輛
    # 所有車、所有車數量
    AllCar = Car.objects.all()
    AllCarN = Car.objects.all().count()
    # 站點可使用
    bike = 0;
    motorcycle = 0;
    bikeN = 999999;
    motorcycleN = 999999;
    if request.method == 'POST':
        # 從0開始
        for i in range(AllCarN):
            if (str(AllCar[i].locate_station) == Place and str(AllCar[i].status) == "正常"):
                if (str(AllCar[i].car_type) == "Bike"):
                    bikeN = i;
                    bike = bike + 1;
                if (str(AllCar[i].car_type) == "motorcycle"):
                    motorcycleN = i;
                    motorcycle = motorcycle + 1
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

        # 建構Order物件
        if Place != None and CarT != None:
            U = User.objects.get(id=user_id)

            # S = Station.objects.get(station_name=Place)  # 暫時用不到
            # print("S is **************",Place) #測試用
            # date1=datetime.now() # 暫時用不到
            # print("date1 is ",date1)
            items = Order.objects.create(order_user=U, order_car=C)


            items.save()
            messages.success(request, "預約成功")
            return redirect('/order/')

    return render(request, "finishrent.html",rent_context)


