from django.shortcuts import render

from item.models import Category, Item
# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    Categories = Category.objects.all()
    return render(request, 'sell/index.html',{
        'Categories': Categories,
        'items': items
    })

def contact(request):
    return render(request, 'sell/contact.html')

def base(request):
    return render(request, 'sell/base.html')