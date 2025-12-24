from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Contact
from .models import GetQuote
from django.contrib import messages


# Create your views here.


def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        uemail=request.POST.get('useremail')
        upass1=request.POST.get('userpass1')
        upass2=request.POST.get('userpass2')
        if upass1!=upass2:
            return HttpResponse("your password and conform password are not same")
        else:
            my_user=User.objects.create_user(uname,uemail,upass1)
            my_user.save()
            return redirect('login')
    return render(request, 'signup.html')

def user_login(request):
    if request.method=='POST':
        uemail=request.POST.get('username')
        upass=request.POST.get('userpass1')
        user = authenticate(request, username=uemail, password=upass)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("User name or password is incorrect!")
    return render(request, 'login.html')

@login_required(login_url='login')
def home(request):
    if request.method=='POST':
        ct_name=request.POST.get('name')
        ct_email=request.POST.get('email')
        ct_subject=request.POST.get('subject')
        ct_message=request.POST.get('message')
        Contact.objects.create(
            name=ct_name,
            email=ct_email,
            subject=ct_subject,
            message=ct_message
        )
        messages.success(request, "Message sent successfully!")
        return redirect('contact')

    return render(request, 'home.html')

def LogoutPage(request):
    logout(request,)
    return redirect('login')

@login_required(login_url='login')
def about(request):
    return render(request, 'about.html')

@login_required(login_url='login')
def services(request):
    return render(request, 'service.html')

@login_required(login_url='login')
def contact(request):
     return render(request, 'contact.html')

@login_required(login_url='login')
def save_form(request):
    if request.method=='POST':
        ct_name=request.POST.get('name')
        ct_email=request.POST.get('email')
        ct_subject=request.POST.get('subject')
        ct_message=request.POST.get('message')
        Contact.objects.create(
            name=ct_name,
            email=ct_email,
            subject=ct_subject,
            message=ct_message
        )
        messages.success(request, "Message sent successfully!")
        return redirect('contact')
    return render(request, "contact.html")

@login_required(login_url='login')
def get_quote(request):
    if request.method=='POST':
        c_name=request.POST.get('name')
        c_email=request.POST.get('email')
        c_phone=request.POST.get('phone')
        c_service=request.POST.get('service')
        c_details=request.POST.get('details')
        GetQuote.objects.create(
            name=c_name,
            email=c_email,
            phone=c_phone,
            service=c_service,
            details=c_details
        )
        messages.success(request, "Your request has been sent successfully!")
       # return redirect('getquote')
        return redirect(request.META.get('HTTP_REFERER', 'getquote'))
    return render(request, 'get_quote.html')

@login_required(login_url='login')
def project(request):
    return render(request, 'projects.html')
