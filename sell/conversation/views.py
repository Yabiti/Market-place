from django.shortcuts import render, redirect, get_list_or_404

from .forms import conversationmessageForm
from item.models import Item
from .models import conversation
# Create your views here.

def new_conversation(request, item_pk):
    item = get_list_or_404(Item, pk=item_pk)


    if item.created_by == request.user:
        return redirect("dashboard:index")
    
    conversations = conversation.objects.filter(item=item).filter(members_in=[request.user.id])

    if conversations:
        pass