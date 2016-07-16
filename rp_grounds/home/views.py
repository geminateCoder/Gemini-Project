from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'home/index.html', context)


def about(request):
    context = {}
    return render(request, 'home/about.html', context)


def goals(request):
    context = {}
    return render(request, 'home/goals.html', context)


def features(request):
    context = {}
    return render(request, 'home/features.html', context)


def staff(request):
    context = {}
    return render(request, 'home/staff.html', context)


def news(request):
    context = {}
    return render(request, 'home/news.html', context)

