from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view(), name="index_page"),
    path('thank-you', views.thank_you, name="thank_you_page"),
]
