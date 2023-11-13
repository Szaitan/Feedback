from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
# Create your views here.


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        data = "This works?"
        return render(request, 'reviews/review.html', {'form': form,
                                                       'data': data})

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Wykorzystując ModelForm możemy użyć skróconej wersji zapisu w postaci:
            # form.save()
            entered_data = form.cleaned_data
            object_to_save = Review(username=entered_data["username"], review_text=entered_data["review_text"],
                                    rating=entered_data["rating"]).save()
            return redirect('thank_you_page')
        return render(request, 'reviews/review.html', {
            'form': form,
        })


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


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you_page.html"
    all_reviews = Review.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ReviewListView(TemplateView):
    template_name = "reviews/review_list.html"

    def get_context_data(self, **kwargs):
        all_reviews = Review.objects.all()
        context = super().get_context_data(**kwargs)
        context["all_reviews"] = all_reviews
        return context


class DetailedReviewListView(TemplateView):
    template_name = "reviews/detailed_review_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(kwargs['data_id'])
        print(type(kwargs['data_id']))
        print(type(Review.objects.get(id=kwargs['data_id'])))
        xyz = Review.objects.get(id=kwargs['data_id'])
        print(xyz.review_text)
        context["data"] = xyz
        # WAŻNE to co przekazujemy do html to dictionary !!! Więc aby dostać się do danych trzeba w temaplacie wezwać
        # nazwę dictionary a nie context !!! W tym wypadku jest to "data" !!!
        return context


# class DetailedReviewListView(View):
#     def get(self, request, data_id):
#         print(data_id)
#         data = Review.objects.get(id=data_id)
#         print(data)
#         return render(request, "reviews/detailed_review_list.html", {
#             "data": data,
#         })
#
