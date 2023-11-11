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
    form = ReviewForm()
    return render(request, 'reviews/review.html', {'form': form})


def thank_you(request):
    return render(request, "reviews/thank_you_page.html")
