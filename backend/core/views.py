import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import Channel, Message, DirectMessage


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['channel_count'] = Channel.objects.count()
    ctx['channel_public'] = Channel.objects.filter(channel_type='public').count()
    ctx['channel_private'] = Channel.objects.filter(channel_type='private').count()
    ctx['channel_direct'] = Channel.objects.filter(channel_type='direct').count()
    ctx['message_count'] = Message.objects.count()
    ctx['message_text'] = Message.objects.filter(message_type='text').count()
    ctx['message_file'] = Message.objects.filter(message_type='file').count()
    ctx['message_image'] = Message.objects.filter(message_type='image').count()
    ctx['directmessage_count'] = DirectMessage.objects.count()
    ctx['directmessage_text'] = DirectMessage.objects.filter(message_type='text').count()
    ctx['directmessage_file'] = DirectMessage.objects.filter(message_type='file').count()
    ctx['directmessage_image'] = DirectMessage.objects.filter(message_type='image').count()
    ctx['recent'] = Channel.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def channel_list(request):
    qs = Channel.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(channel_type=status_filter)
    return render(request, 'channel_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def channel_create(request):
    if request.method == 'POST':
        obj = Channel()
        obj.name = request.POST.get('name', '')
        obj.channel_type = request.POST.get('channel_type', '')
        obj.description = request.POST.get('description', '')
        obj.member_count = request.POST.get('member_count') or 0
        obj.created_by = request.POST.get('created_by', '')
        obj.active = request.POST.get('active') == 'on'
        obj.save()
        return redirect('/channels/')
    return render(request, 'channel_form.html', {'editing': False})


@login_required
def channel_edit(request, pk):
    obj = get_object_or_404(Channel, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.channel_type = request.POST.get('channel_type', '')
        obj.description = request.POST.get('description', '')
        obj.member_count = request.POST.get('member_count') or 0
        obj.created_by = request.POST.get('created_by', '')
        obj.active = request.POST.get('active') == 'on'
        obj.save()
        return redirect('/channels/')
    return render(request, 'channel_form.html', {'record': obj, 'editing': True})


@login_required
def channel_delete(request, pk):
    obj = get_object_or_404(Channel, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/channels/')


@login_required
def message_list(request):
    qs = Message.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(sender__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(message_type=status_filter)
    return render(request, 'message_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def message_create(request):
    if request.method == 'POST':
        obj = Message()
        obj.sender = request.POST.get('sender', '')
        obj.channel_name = request.POST.get('channel_name', '')
        obj.content = request.POST.get('content', '')
        obj.message_type = request.POST.get('message_type', '')
        obj.sent_at = request.POST.get('sent_at') or None
        obj.pinned = request.POST.get('pinned') == 'on'
        obj.save()
        return redirect('/messages/')
    return render(request, 'message_form.html', {'editing': False})


@login_required
def message_edit(request, pk):
    obj = get_object_or_404(Message, pk=pk)
    if request.method == 'POST':
        obj.sender = request.POST.get('sender', '')
        obj.channel_name = request.POST.get('channel_name', '')
        obj.content = request.POST.get('content', '')
        obj.message_type = request.POST.get('message_type', '')
        obj.sent_at = request.POST.get('sent_at') or None
        obj.pinned = request.POST.get('pinned') == 'on'
        obj.save()
        return redirect('/messages/')
    return render(request, 'message_form.html', {'record': obj, 'editing': True})


@login_required
def message_delete(request, pk):
    obj = get_object_or_404(Message, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/messages/')


@login_required
def directmessage_list(request):
    qs = DirectMessage.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(sender__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(message_type=status_filter)
    return render(request, 'directmessage_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def directmessage_create(request):
    if request.method == 'POST':
        obj = DirectMessage()
        obj.sender = request.POST.get('sender', '')
        obj.receiver = request.POST.get('receiver', '')
        obj.content = request.POST.get('content', '')
        obj.sent_at = request.POST.get('sent_at') or None
        obj.read = request.POST.get('read') == 'on'
        obj.message_type = request.POST.get('message_type', '')
        obj.save()
        return redirect('/directmessages/')
    return render(request, 'directmessage_form.html', {'editing': False})


@login_required
def directmessage_edit(request, pk):
    obj = get_object_or_404(DirectMessage, pk=pk)
    if request.method == 'POST':
        obj.sender = request.POST.get('sender', '')
        obj.receiver = request.POST.get('receiver', '')
        obj.content = request.POST.get('content', '')
        obj.sent_at = request.POST.get('sent_at') or None
        obj.read = request.POST.get('read') == 'on'
        obj.message_type = request.POST.get('message_type', '')
        obj.save()
        return redirect('/directmessages/')
    return render(request, 'directmessage_form.html', {'record': obj, 'editing': True})


@login_required
def directmessage_delete(request, pk):
    obj = get_object_or_404(DirectMessage, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/directmessages/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['channel_count'] = Channel.objects.count()
    data['message_count'] = Message.objects.count()
    data['directmessage_count'] = DirectMessage.objects.count()
    return JsonResponse(data)
