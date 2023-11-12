from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReviewForm
from .models import Review
from django.views import View
# Create your views here.


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, 'reviews/review.html', {'form': form})

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Wykorzystując ModelForm możemy użyć skróconej wersji zapisu w postaci:
            # form.save()
            entered_data = form.cleaned_data
            object_to_save = Review(username=entered_data["username"], review_text=entered_data["review_text"],
                                    rating=entered_data["rating"]).save()
            return redirect('thank_you_page')
        return render(request, 'reviews/review.html', {'form': form})


# def index(request):
#     print(Review.objects.get(id=1))
#     if request.method == "POST":
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             # Wykorzystując ModelForm możemy użyć skórconej wersji zapisu w postaci:
#             # form.save()
#             entered_data = form.cleaned_data
#             print(entered_data)
#             object_to_save = Review(username=entered_data["username"], review_text=entered_data["review_text"],
#                                     rating=entered_data["rating"]).save()
#             return redirect('thank_you_page')
#     else:
#         form = ReviewForm()
#     return render(request, 'reviews/review.html', {'form': form})
#     # Cała konstrukcja powyżej opiera się na form.
#     # Jeśli jest to POST ale nie jest valid to zostaje ta forma przekazana a nie pusta.


def thank_you(request):
    return render(request, "reviews/thank_you_page.html")
