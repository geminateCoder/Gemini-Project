from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


@login_required
def dashboard(request):
    context = {
        "title": "RPGround Dashboard"
    }
    return render(request, 'dashboard.html', context)


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST or None, request.FILES or None, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard')
    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance=profile)
    context = {'form':form,
               "title": "User Settings"}

    return render(request, 'settings.html', context)


def userProfile(request, id):
    instance = get_object_or_404(User, username=id)
    context = {
        "instance":instance
    }
    return render(request, "userProfile.html", context)

