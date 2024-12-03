from django.shortcuts import render, redirect

from item.models import Category, Item
from .forms import SignUpForm
# Create your views here.

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

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
        
        return redirect('login/')
    else:
        form = SignUpForm()
    return render(request, 'sell/signup.html', {
        'form': form
    })