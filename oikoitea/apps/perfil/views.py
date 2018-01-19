from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .forms import *
from .models import UserProfile

def get_user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, "perfil/user_perfil.html", {"user":user})

@login_required
def update_profile(request):
    args = {}
    user = request.user
    if request.method == 'POST':
        user_form         = UpdateUserForm(request.POST, instance=user)
        user_profile        = user.userprofile
        user_profile.save()

        user_profile_form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)

        if user_form.is_valid() and user_profile_form.is_valid():
            user                = user_form.save()
            user_profile        = user_profile_form.save()
            user_profile.user   = user

            user_profile.save()

            return HttpResponseRedirect(reverse("perfil:perfil_username", args=[user.username]))
    else:
        user_form         = UpdateUserForm(instance=user)
        UserProfile.objects.get_or_create(user=request.user)
        user_profile_form = UserProfileForm(instance=user.userprofile)

    args['user_form'] = user_form
    args['profile_form'] = user_profile_form
    return render(request, 'perfil/update_profile.html', args)

