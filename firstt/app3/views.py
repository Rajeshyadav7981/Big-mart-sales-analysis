from django.shortcuts import render
from .models import sales
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from joblib import load
def index(request):
    return render(request,'index.html')
def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return render(request,'index.html')
        





    return render(request,'signup.html')

def login(request):

    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:

            '''k=load('/savedmodel.joblib')
            return HttpResponse(k.predict([[9,34,7,0.98,0,0,0,0,0,0,1,1,1,0,0,1,0,0,1,1,1,0,0,1,0,1,0,1,1,0,0]]).reshape(1,-1))'''
            return render(request,'home.html')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render(request,'login.html')


def result(request):
    if request.method=='POST':
        Item_W=request.POST.get('Item_Weight')
        Item_M =request.POST.get('Item_MRP')
        Item_V=request.POST.get('Item_Visibility')
        Item_Fat=request.POST.get('Item_Fat_Content')
        Outlet_L=request.POST.get('Outlet_Location_Type')
        Outlet_T=request.POST.get('Outlet_Type')
        Outlet_S=request.POST.get('Outlet_Size')

        resu=0
        li=[int(float(Item_W)),0,int(float(Item_M)),0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0]
        if Item_Fat=='low fat':
            li[3]==1
        elif Item_Fat=='regular':
            li[4]=1
        if Outlet_L=='tyre1':
            li[8]=1
        elif Outlet_L=='tyre2':
            li[9]=1
        elif Outlet_L=='tyre3':
            li[10]=1
        if Outlet_S=='high':
            li[11]=1
        elif Outlet_S=='medium':
            li[12]=1
        elif Outlet_S=='small':
            li[13]=1
        if Outlet_T=='grocery store':
            li[14]=1
        elif Outlet_T=='supermarket tyre1':
            li[15]=1
        elif Outlet_T=='supermarket tyre2':
            li[16]=1
        elif Outlet_T=='supermarket tyre3':
            li[17]=1
        for i in range(len(li)):
            if li[i]==None:
                li[i]=0
            else:
                li[i]=int(li[i])
        print(li)
        kk=load('machinemodel/rand.joblib')


        resu=kk.predict([li]).reshape(-1,1)
        resu=resu[0]
        resu=resu[0]

        data=sales(Item_Weight=Item_W,Item_MRP=Item_M,Item_Visibility=Item_V,Item_Fat_Content=Item_Fat,Outlet_location_type=Outlet_L,Outlet_Type=resu,Outlet_Size=Outlet_S)
        data.save()
        task=sales.objects.all()
        context={'tas':task,'res':resu}

        return render(request,'final.html',context)
def charts(request):
    return render(request,'pie.html')
def userdata(request):
    us=User.objects.all()
    return render(request,'users.html',{'use':us})








'''<!--Item_Weight               float64
Item_Visibility           float64
Item_MRP                  float64
Item_Fat_Content_0          int64
Item_Fat_Content_1          int64
Item_Fat_Content_2          int64
Item_Fat_Content_3          int64
Item_Fat_Content_4          int64
Outlet_Location_Type_0      int64
Outlet_Location_Type_1      int64
Outlet_Location_Type_2      int64
Outlet_Size_0               int64
Outlet_Size_1               int64
Outlet_Size_2               int64
Outlet_Type_0               int64
Outlet_Type_1               int64
Outlet_Type_2               int64
Outlet_Type_3               int64
Item_Type_Combined_0        int64
Item_Type_Combined_1        int64
Item_Type_Combined_2        int64
Outlet_0                    int64
Outlet_1                    int64
Outlet_2                    int64
Outlet_3                    int64
Outlet_4                    int64
Outlet_5                    int64
Outlet_6                    int64
Outlet_7                    int64
Outlet_8                    int64
Outlet_9                    int64-->'''