from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view(), name="index_page"),
    path('thank-you', views.ThankYouView.as_view(), name="thank_you_page"),
    path('review-list', views.ReviewListView.as_view(), name="review_list_page"),
    path('review-list/<int:pk>', views.DetailedReviewListView.as_view(), name="detailed_review_list_page")
]
