from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView


# Create your views here.

# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thank-you"
#
#     def form_valid(self, form):
#         entered_data = form.cleaned_data
#         object_to_save = Review(username=entered_data["username"], review_text=entered_data["review_text"],
#                                 rating=entered_data["rating"]).save()
#         return super().form_valid(form)


# Podstawowa forma View klasy
class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        data = "This works?"
        return render(request, 'reviews/review.html', {'form': form,
                                                       'data': data})

    def post(self, request):
        form = ReviewForm(request.POST) #Tutaj wsadzamy dane uzyskane w request.POST w celu ich walidacji
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


class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "all_reviews"
    # Normalnie gdy context_object_name nie jest ustalone, variable zawierajace dane to object_list

    def get_queryset(self):
        context = super().get_queryset()
        context = context.filter(rating__gte=2)
        return context

# class DetailedReviewListView(DetailView):
#     template_name = "reviews/detailed_review_list.html"
#     model = Review
#     context_object_name = "data"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     xyz = Review.objects.get(id=kwargs['data_id'])
    #     context["data"] = xyz
    #     # WAŻNE to co przekazujemy do html to dictionary !!! Więc aby dostać się do danych trzeba w temaplacie wezwać
    #     # nazwę dictionary a nie context !!! W tym wypadku jest to "data" !!!
    #     return context


class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        request.session["favorite_review"] = int(review_id)
        return redirect(reverse("detailed_review_list_page", args=[review_id]))


class DetailedReviewListView(View):
    def get(self, request, pk):
        data = Review.objects.get(id=pk)

        is_favorite = False
        # print(f"data.id = {data.id } and request.session == {request.session['favorite_review']}")
        if data.id == request.session.get("favorite_review"):
            is_favorite = True

        return render(request, "reviews/detailed_review_list.html", {
            "data": data,
            "is_favorite": is_favorite
        })


