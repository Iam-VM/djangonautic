from django.shortcuts import render
from .models import Articles
from django.contrib.auth.decorators import login_required

articles = Articles.objects.all().order_by('date')


def article_list(req):
    return render(req, 'articles/articlesList.html', {'articles': articles})


def article_details(req, slug):
    # return HttpResponse("<h1>{}</h1>".format(slug))
    article = Articles.objects.get(slug=slug)
    return render(req, 'articles/articleDetails.html', {'article': article})


@login_required(login_url='/accounts/login')
def article_create(req):
    return render(req, 'articles/article_create.html')
