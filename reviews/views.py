from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.


def index(request):
    if request.method == "POST":
        entered_name = request.POST['username']
        print(entered_name)
        return redirect('thank_you_page')
    return render(request, 'reviews/review.html')


def thank_you(request):
    return render(request, "reviews/thank_you_page.html")
