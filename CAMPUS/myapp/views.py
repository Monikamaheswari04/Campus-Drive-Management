from django.shortcuts import redirect, render
from .models import Userdata,Companyinfo,Register

from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request,method=['GET','POST']):
    if request.method=="POST":
       email=request.POST.get('email')
       password=request.POST.get('password')
       confirm_password=request.POST.get('confirm_password')

       user=Userdata.objects.filter(email=email)

       if user.exists():
           messages.info(request,"User is already exists")
       elif password !=confirm_password:
           messages.info(request,"Password does not match")
       else:
           Userdata.objects.create(email=email,password=password)
           return render(request,'login.html')

    return render(request,'signup.html')



def login(request,method=['GET','POST']):
    if request.method=="POST":
       email=request.POST.get('email')
       password=request.POST.get('password')
      

       user=Userdata.objects.filter(email=email,password=password)

       if user.exists():
           return redirect('/home/')
       else:
           messages.error(request,'Email and Password are incorrect')
           
   

    return render(request,'login.html')

def home(request):
    company_info=Companyinfo.objects.all()
    return render (request,'home.html',{'campanies':company_info})

def companyapply(request,id):
    company = Companyinfo.objects.get(id=id)
    return render(request,'register.html',{'company':company})

def register(request):
    if request.method=='POST':
        c_n=request.POST.get('cname')
        n=request.POST.get('name')
        a=request.POST.get('age')
        g=request.POST.get('gender')
        phone=request.POST.get('contactnumber')
        res=request.POST.get('resume')
        Register.objects.create(c_name=c_n,name=n,age=a,gender=g,contact=phone,resume=res)
    return render(request,'success.html')
    


    

    



