from django.shortcuts import render, redirect, get_list_or_404

from item.models import Item
# Create your views here.

def new_conversation(request, item_pk):
    item = get_list_or_404(Item, pk=item_pk)


    if item.created_by == request.user:
        return redirect("dashboard:index")