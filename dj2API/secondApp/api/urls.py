from django.urls import path
from .views import secondFunction
from .views import thirdFunction

urlpatterns = [
    path('second/', secondFunction),
    path('third/', thirdFunction),
]