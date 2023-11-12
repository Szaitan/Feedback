from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReviewForm

# Create your views here.


def index(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            entered_name = form.cleaned_data
            print(entered_name["username"])
            return redirect('thank_you_page')
    else:
        form = ReviewForm()
    return render(request, 'reviews/review.html', {'form': form})
    # Cała konstrukcja powyżej opiera się na form.
    # Jeśli jest to POST ale nie jest valid to zostaje ta forma przekazana a nie pusta.


def thank_you(request):
    return render(request, "reviews/thank_you_page.html")
