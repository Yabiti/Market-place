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


def signup(request):
    if request == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid:
            form.save()

            return redirect('/login/')
    form = SignUpForm()

    return render(request, 'core/signup.html', {
        'form': form
    })