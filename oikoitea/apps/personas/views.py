from django.shortcuts import render

def profesionales_index(request):
    return render(request, 'personas/profesionales_index.html', {})