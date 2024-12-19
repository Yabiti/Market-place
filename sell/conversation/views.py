from django.shortcuts import render, redirect, get_list_or_404

from .forms import ConversationMessageForm

from item.models import Item
from .models import Conversation
# Create your views here.

def new_conversation(request, item_pk):
    item = get_list_or_404(Item, pk=item_pk)


    if item.created_by == request.user:
        return redirect("dashboard:index")
    
    conversations = conversation.objects.filter(item=item).filter(members_in=[request.user.id])

    if conversations:
        pass

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk=item_pk)
        else:
            form = ConversationMessageForm()


        return render(request, 'conversation/new.html',{
            'form': form
        })