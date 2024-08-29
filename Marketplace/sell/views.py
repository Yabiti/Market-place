from django.shortcuts import render

from . import Category, Item
# Create your views here.
def index(request):
    items = Item.objects.filter(is_sild=False)[0:6]
    return render(request, 'sell/index.html')

def contact(request):
    return render(request, 'sell/contact.html')

def base(request):
    return render(request, 'sell/base.html')