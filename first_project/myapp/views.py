from django.shortcuts import render
from myapp.forms import *
from django.template import loader
from django.http import HttpResponse
from django.core.urlresolvers import reverse


def responseform(request):
 #if form is submitted
     if request.method == 'POST':
        myForm = MyForm(request.POST)
        # import pdb
        # pdb.set_trace()
        if myForm.is_valid():
            Name = myForm.cleaned_data['Name']
            Email_id = myForm.cleaned_data['Email_id']
            Age = myForm.cleaned_data['Age']
            Feedback = myForm.cleaned_data['Feedback']
            Food_Quality = myForm.cleaned_data['Food_Quality']
            Location_Visited = myForm.cleaned_data['Location_Visited']
            context = {
            'Name': Name,
            'Email_id': Email_id,
            'Age': Age,
            'Feedback': Feedback,
            'Food_Quality': Food_Quality,
            'Location_Visited': Location_Visited,
            }

            obj = Restaurant_review.objects.create(Name=Name,Email_id=Email_id,Age=Age,Feedback=Feedback,Food_Quality=Food_Quality,Location_Visited=Location_Visited)

            template = loader.get_template('myapp/thankyou.html')

            return HttpResponse(template.render(context, request))



     else:
         form = MyForm()

     return render(request, 'myapp/responseform.html', {'form':form});


def AirDetails(request):
    if request.method == 'POST':
        # import pdb
        # pdb.set_trace()
        form1 = AirModelForm(request.POST)
        if form1.is_valid():

            a = form1.save()
            air = bookingAirTicket.objects.all()
            context = {'air':air,'form1':form1}

            template = loader.get_template('myapp/display_booking.html')

            return HttpResponse(template.render(context, request))

    else:
        formAir = AirModelForm()

    return render(request, 'myapp/booking_details.html',{'formAir':formAir})            




