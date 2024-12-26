from django.contrib import admin
from .models import Conversation, ConversationMessage

class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'created_at', 'modified_at')
    search_fields = ('item__name',)

class ConversationMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'conversation', 'content', 'created_at', 'created_by')
    search_fields = ('conversation__id', 'content', 'created_by__username')

admin.site.register(Conversation, ConversationAdmin)
admin.site.register(ConversationMessage, ConversationMessageAdmin)
