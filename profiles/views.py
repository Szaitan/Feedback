from django.shortcuts import render, redirect
from django.views import View
from .forms import ProfileForm
from .models import UserProfile

# Create your views here.


class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {
            'form': form
        })

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES)
        print(form.errors.as_data())
        if form.is_valid():
            user = UserProfile(image=request.FILES["image"])
            user.save()
            return redirect('/profiles')
        return redirect("/profiles", {
            'form': form
        })
