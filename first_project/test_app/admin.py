from django.contrib import admin
from .models import Author, Publisher, Book
# Register your models here.


""" Option 1 - Basic """
admin.site.register(Author)    
# admin.site.register(Book)    
                            
""" Option 2 - Allows customizing Django admin behavior """
class BookInline(admin.TabularInline):
    model = Book
    readonly_fields = ['Publishers']


class PublisherAdmin(admin.ModelAdmin):
    list_display=['Name']
    list_filter=['Address']
    # fields = ['Name','Address','City','State','Country','Website']
    fieldsets=(
        (None,{
        'fields':['Name','Address','City','Country']
        }),
        ('Website',{
        'fields':['Website']
        })
    )    
    search_fields=['State']
    

    inlines = [
        BookInline,
    ]
admin.site.register(Publisher, PublisherAdmin)

""" Option 3 -- Decorator """




@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['Title','Publishers']
    list_filter=['Publishers']
    search_fields=['Title']
    






    

