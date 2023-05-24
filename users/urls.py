from .views import SignUpPageView
from django.urls import path

urlpatterns = [
    path('signup/', SignUpPageView.as_view(), name='signup'),
]