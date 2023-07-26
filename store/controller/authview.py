from unicodedata import category
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from store.forms import CustomUserForm

# Create your views here.
def logoutpage (request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'Logged out successfully')
    return redirect('/')



def register(request):
    form=CustomUserForm()
    if request.method =='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registered successfully, Login to continue')
            return redirect('loginpage')
    context={'form':form}
    return render(request,"store/auth/register.html",context)

def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already loged in')
        return redirect('/')
    else: 
        if request.method=='POST':
            name = request.POST.get('uname')
            passd = request.POST.get('pass')

            user=authenticate(request,username=name,password=passd)

            if user is not None:
                login(request,user)
                messages.success(request,'Logged in successfully')
                return redirect('/')
            else:
                messages.error(request,'Error in Username or Password')
                return redirect('/login')

    return render(request,'store/auth/loginpage.html')