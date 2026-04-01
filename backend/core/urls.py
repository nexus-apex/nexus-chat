from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('channels/', views.channel_list, name='channel_list'),
    path('channels/create/', views.channel_create, name='channel_create'),
    path('channels/<int:pk>/edit/', views.channel_edit, name='channel_edit'),
    path('channels/<int:pk>/delete/', views.channel_delete, name='channel_delete'),
    path('messages/', views.message_list, name='message_list'),
    path('messages/create/', views.message_create, name='message_create'),
    path('messages/<int:pk>/edit/', views.message_edit, name='message_edit'),
    path('messages/<int:pk>/delete/', views.message_delete, name='message_delete'),
    path('directmessages/', views.directmessage_list, name='directmessage_list'),
    path('directmessages/create/', views.directmessage_create, name='directmessage_create'),
    path('directmessages/<int:pk>/edit/', views.directmessage_edit, name='directmessage_edit'),
    path('directmessages/<int:pk>/delete/', views.directmessage_delete, name='directmessage_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
