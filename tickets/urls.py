from django.urls import path
from .views import *

urlpatterns = [
    path('welcome/', WelcomeView.as_view()),
    path('menu/', MenuView.as_view()),
    path('get_ticket/<str:ticket_type>', GetTicket.as_view())
]
