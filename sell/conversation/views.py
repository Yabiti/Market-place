from django.shortcuts import render, redirect, get_object_or_404
from .forms import ConversationMessageForm
from item.models import Item
from .models import Conversation

def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    # Check if the item is created by the current user
    if item.created_by == request.user:
        return redirect("dashboard:index")

    # Check if a conversation already exists for this item and user
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    # If a conversation exists, redirect to the detail view of the first conversation
    if conversations.exists():
        return redirect('conversation:detail', pk=conversations.first().id)

    # Handle POST request to create a new conversation and message
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
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

    # Render the new conversation form
    return render(request, 'conversation/new.html', {'form': form})
