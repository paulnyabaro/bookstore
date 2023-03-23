from django.urls import path
from .views import AboutPageView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]