from django.shortcuts import render
from .forms import *
from django.template import loader
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from .tasks import *
from django.contrib.auth import authenticate
# Create your views here.


def Profile_User(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'ProfileUser/user_regi.html',{'form':form})  
            
    else:
        form = UserForm()

    return render(request, 'ProfileUser/User_login.html',{'form':form})  


def User_login(request):

     if request.method == 'POST':
        form = User_Login_form(request.POST)
        if form.is_valid():
            # import pdb ; pdb.set_trace()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            otp = form.cleaned_data['otp']

            user = authenticate(username=username,password=password)
            print user
            if not user:
                error="invalid user"
            elif user.is_authenticated():
                if user.user_id.otp == otp:
                    login_form.delay(user.email)
                    return render(request, 'ProfileUser/logged.html', {'username':username,'password':password,'otp':otp});     
                else:
                    error="invalid otp"
                    return render(request, 'ProfileUser/login_form.html', {'form':form,'error':error});    

            # user = User.objects.get(username=username,password=password)
            # login_form.delay(user.email)

            return render(request, 'ProfileUser/login_form.html', {'form':form,'error':error});    
            
     else:
         form = User_Login_form()

     return render(request, 'ProfileUser/login_form.html', {'form':form});

