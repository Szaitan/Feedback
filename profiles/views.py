from django.shortcuts import render, redirect
from django.views import View

# Create your views here.


def store_file(file):
    with open(f"temp/{file.name}", "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)


class CreateProfileView(View):
    def get(self, request):
        return render(request, "profiles/create_profile.html")

    def post(self, request):
        store_file(request.FILES["image"])
        return redirect("/profiles")
