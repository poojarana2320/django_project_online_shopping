from django.shortcuts import render
from django.http import HttpResponse
from . models import * 
from django.template import loader
from django.views import View
# Create your views here.

def Author_view(request):
    if request.method == 'GET':
        author = Author.objects.all()
        # return HttpResponse(author)
        template = loader.get_template('test_app/authors_name.html')
        context = {
            'author': author,
        }
        return HttpResponse(template.render(context, request))

     
def Publisher_view(request):
    if request.method == 'GET':
        publisher = Publisher.objects.all()
        template = loader.get_template('test_app/publisher_info.html')
        context = {
            'publisher': publisher,
        }
        return HttpResponse(template.render(context, request))        




class Book_view_class(View):
    def get(self,request):
        book = Book.objects.all()
        template = loader.get_template('test_app/book_info.html')
        context = {
            'book': book,
        }
        return HttpResponse(template.render(context, request))
