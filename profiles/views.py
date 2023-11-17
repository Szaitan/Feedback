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

        if form.is_valid():
            user = UserProfile(image=request.FILES["image"])
            user.save()
            return redirect('/profiles')
        # Ważne !!! gdy for validate jest False trzeba użyć render a nie redirect aby widzieć uwagi
        return render(request, "profiles/create_profile.html", {'form': form})


class UserProfiles(View):
    def get(self, request):
        list_w_users = UserProfile.objects.all()
        return render(request, "profiles/user_profiles.html", {
            "list_with_users": list_w_users
        })
