from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article, Auteur

# Create your views here.

def home(request):
    return HttpResponse('<h1>Hello Word !!!</h1>')


def list_articles(request):

    articles = Article.objects.all()
    auteurs = Auteur.objects.all()

    articles_filtre = None

    if 'listes_auteur' in request.POST:
        request.session['auteur_selected'] = int(request.POST.get('listes_auteur'))
        articles_filtre = Article.objects.filter(auteur=Auteur.objects.get(id=request.session['auteur_selected']))

    context = {'articles': articles, 'auteurs': auteurs, 'articles_filtre': articles_filtre}

    return render(request, 'firstapp/articles.html', context=context)

def details_article(request, id_article):

    #article = Article.objects.get(id_article)
    article = get_object_or_404(Article, id_article)
    context = {'art': article}
    return render(request, 'firstapp/details_articles.html', context=context)