from django.urls import path
from .views import MessageListCreateAPIView

urlpatterns = [
    path('api/messages/', MessageListCreateAPIView.as_view(), name='message-api'),
]