from django.db import models

class Channel(models.Model):
    name = models.CharField(max_length=255)
    channel_type = models.CharField(max_length=50, choices=[("public", "Public"), ("private", "Private"), ("direct", "Direct")], default="public")
    description = models.TextField(blank=True, default="")
    member_count = models.IntegerField(default=0)
    created_by = models.CharField(max_length=255, blank=True, default="")
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Message(models.Model):
    sender = models.CharField(max_length=255)
    channel_name = models.CharField(max_length=255, blank=True, default="")
    content = models.TextField(blank=True, default="")
    message_type = models.CharField(max_length=50, choices=[("text", "Text"), ("file", "File"), ("image", "Image"), ("link", "Link")], default="text")
    sent_at = models.DateField(null=True, blank=True)
    pinned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.sender

class DirectMessage(models.Model):
    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255, blank=True, default="")
    content = models.TextField(blank=True, default="")
    sent_at = models.DateField(null=True, blank=True)
    read = models.BooleanField(default=False)
    message_type = models.CharField(max_length=50, choices=[("text", "Text"), ("file", "File"), ("image", "Image")], default="text")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.sender
