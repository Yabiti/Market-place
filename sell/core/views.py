from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from item.models import Category, Item
from  .forms import SignUpForm
# Create your views here.


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, "core/index.html", {
        'catego ries': categories,
        'items': items
    })

def contact(request):
    return render(request, "core/contact.html")

