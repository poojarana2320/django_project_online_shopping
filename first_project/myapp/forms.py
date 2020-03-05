from django import forms
from django.forms import ModelForm , TextInput , Textarea
from . models import *
from django.forms.widgets import RadioSelect
from datetime import datetime, date

food_Quality=(
        ('excellent','Excellent'),
        ('good','Good'),
        ('average','Average'),
        ('dissatisfied','Dissatisfied')
        )

Location_Choices=(
        ('Location1','Location1'),
        ('Location2','Location2'),
        ('Location3','Location3')
        )

class MyForm(forms.Form):
    Name=forms.CharField(
       label="Your Name", widget=forms.TextInput(attrs={'class': 'form_input'}))
    Email_id=forms.EmailField(
       label="Email", widget=forms.TextInput(attrs={'class': 'form_input'}))
    Age=forms.IntegerField(
       label="Age", widget=forms.TextInput(attrs={'class': 'form_input'}))
    Feedback=forms.CharField(label="Feedback",widget=forms.Textarea(attrs={'width':"100%", 'cols' : "80", 'rows': "20", 'class': 'form_textarea' }))
    Food_Quality=forms.ChoiceField(choices=food_Quality,label="Food_Quality",widget=forms.RadioSelect)
    Location_Visited=forms.ChoiceField(choices=Location_Choices,label="Location_Visited",widget=forms.RadioSelect)


class DateInput(forms.DateInput):
    input_type = 'date'
    

class AirModelForm(ModelForm):
    class Meta:
        model = bookingAirTicket
        fields = '__all__'   
        widgets = {
            'Name': TextInput(attrs={'class': 'form_input'}),
            'Email_id': TextInput(attrs={'class': 'form_input'}),
            'Age': TextInput(attrs={'class': 'form_input'}),
            'Address': Textarea(attrs={'width':"100%", 'cols' : "80", 'rows': "20", 'class': 'form_textarea'}),
            'Mobile': TextInput(attrs={'class': 'form_input'}),
            'Travel_From_Date': DateInput(attrs={'class': 'form_input'}),
            'Travel_To_Date': DateInput(attrs={'class': 'form_input'}),
            'Travel_From': TextInput(attrs={'class': 'form_input'}),
            'Travel_To': TextInput(attrs={'class': 'form_input'}),
            'No_of_person': TextInput(attrs={'class': 'form_input'})
        }

    # def clean(self):
    #    cd=self.cleaned_data
    #    if cd.get('Travel_To_Date')<datetime.now().date():
    #        msg="Date value should should not today's date"
    #        # raise ValidationError("Date value should should be equal to or greater than today's date")
    #        self.add_error('Travel_To_Date',msg)
    #    return self.cleaned_data    

