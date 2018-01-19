from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse

@login_required
def index(request):
    return render(request, 'home/index.html', {})