from django.shortcuts import render
from .forms import *
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User
		
def Registration_View(request):
    if request.method == 'POST':
        form = Registration_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirmpassword = form.cleaned_data['confirmpassword']
            mobileno = form.cleaned_data['mobileno']
            address = form.cleaned_data['address']
            country = form.cleaned_data['country']

            if password == confirmpassword:
            	# import pdb
            	# pdb.set_trace()

	            obj = User.objects.create(username=username,first_name=first_name,last_name=last_name,email=email,password=password)

	            reg = Registration.objects.create(user_id=obj ,mobileno=mobileno,address=address,country=country)

                return render(request, 'UserProfile/registration_sucess.html',{'username':username,'first_name':first_name,'last_name':last_name,'email':email,'password':password,'confirmpassword':confirmpassword,'mobileno':mobileno,'address':address,'country':country})  
            
    else:
        form = Registration_form()

    return render(request, 'UserProfile/registration__form.html',{'form':form})  	