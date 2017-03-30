from django.shortcuts import render


def index(request):
    context = {'name': 'Fellipe'}
    return render(request, 'index.html', context)
