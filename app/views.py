
from django.shortcuts import render, redirect


def home(request):
    my_name = "Augustine"
    context = {'my_name': my_name,}
    return render(request, 'home.html', context)