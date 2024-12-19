from django.contrib import admin

from .models import conversation, conversationmessage
# Register your models here.

admin.site.register(conversation)
admin.site.register(conversationmessage)