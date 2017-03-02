from .models import NewsPost
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect


def index(request):
    context = {
        "title": "RolePlayground BETA"
    }
    if request.user.is_authenticated():
        return redirect('/dashboard')
    return render(request, 'home/index.html', context)


def about(request):
    context = {
        "title": "About RPground"
    }
    return render(request, 'home/about.html', context)


def goals(request):
    context = {
        "title": "Our Goals"
    }
    return render(request, 'home/goals.html', context)


def features(request):
    context = {
        "title": "Our Features"
    }
    return render(request, 'home/features.html', context)


def staff(request):
    context = {
        "title": "Staff Members"
    }
    return render(request, 'home/staff.html', context)


def news(request):
    news_list = NewsPost.objects.all().order_by("-timestamp")
    paginator = Paginator(news_list, 4) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news = paginator.page(paginator.num_pages)
    context = {
        "news": news,
        "title": "RPground News"
    }
    return render(request, 'home/news.html', context)

