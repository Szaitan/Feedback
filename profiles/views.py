from django.shortcuts import render, redirect
from django.views import View
from .forms import ProfileForm

# Create your views here.


def store_file(file):
    with open(f"temp/{file.name}", "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)


class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {
            'form': form
        })

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            store_file(request.FILES["image"])
            return redirect('/profiles')
        return redirect("/profiles", {
            'form': form
        })
