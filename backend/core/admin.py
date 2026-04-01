from django.contrib import admin
from .models import Channel, Message, DirectMessage

@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ["name", "channel_type", "member_count", "created_by", "active", "created_at"]
    list_filter = ["channel_type"]
    search_fields = ["name", "created_by"]

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["sender", "channel_name", "message_type", "sent_at", "pinned", "created_at"]
    list_filter = ["message_type"]
    search_fields = ["sender", "channel_name"]

@admin.register(DirectMessage)
class DirectMessageAdmin(admin.ModelAdmin):
    list_display = ["sender", "receiver", "sent_at", "read", "message_type", "created_at"]
    list_filter = ["message_type"]
    search_fields = ["sender", "receiver"]
