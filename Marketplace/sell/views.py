from django.shortcuts import render

from item.models import Category, Item, form
# Create your views here.

from .views
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'sell/index.html',{
        'categories': categories,
        'items': items
    })

def contact(request):
    return render(request, 'sell/contact.html')

def base(request):
    return render(request, 'sell/base.html')