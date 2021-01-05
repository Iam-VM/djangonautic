from django.shortcuts import render, redirect
from .models import Articles
from django.contrib.auth.decorators import login_required
from .forms import CreateArticle

articles = Articles.objects.all().order_by('date')


def article_list(req):
    return render(req, 'articles/articlesList.html', {'articles': articles})


def article_details(req, slug):
    # return HttpResponse("<h1>{}</h1>".format(slug))
    article = Articles.objects.get(slug=slug)
    return render(req, 'articles/articleDetails.html', {'article': article})


@login_required(login_url='/accounts/login')
def article_create(req):
    if req.method == 'POST':
        form = CreateArticle(req.POST, req.FILES)
        instance = form.save(commit=False)
        instance.author = req.user
        instance.save()
        return redirect('articles:list')
    else:
        form = CreateArticle()
    return render(req, 'articles/article_create.html', {'form': form})
