from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Channel, Message, DirectMessage
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusChat with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexuschat.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if Channel.objects.count() == 0:
            for i in range(10):
                Channel.objects.create(
                    name=f"Sample Channel {i+1}",
                    channel_type=random.choice(["public", "private", "direct"]),
                    description=f"Sample description for record {i+1}",
                    member_count=random.randint(1, 100),
                    created_by=f"Sample {i+1}",
                    active=random.choice([True, False]),
                )
            self.stdout.write(self.style.SUCCESS('10 Channel records created'))

        if Message.objects.count() == 0:
            for i in range(10):
                Message.objects.create(
                    sender=f"Sample {i+1}",
                    channel_name=f"Sample Message {i+1}",
                    content=f"Sample content for record {i+1}",
                    message_type=random.choice(["text", "file", "image", "link"]),
                    sent_at=date.today() - timedelta(days=random.randint(0, 90)),
                    pinned=random.choice([True, False]),
                )
            self.stdout.write(self.style.SUCCESS('10 Message records created'))

        if DirectMessage.objects.count() == 0:
            for i in range(10):
                DirectMessage.objects.create(
                    sender=f"Sample {i+1}",
                    receiver=f"Sample {i+1}",
                    content=f"Sample content for record {i+1}",
                    sent_at=date.today() - timedelta(days=random.randint(0, 90)),
                    read=random.choice([True, False]),
                    message_type=random.choice(["text", "file", "image"]),
                )
            self.stdout.write(self.style.SUCCESS('10 DirectMessage records created'))
