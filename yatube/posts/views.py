from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Привет, пока тут располагается пустая строка!')


def groups_posts(request, slug):
    return HttpResponse(f'Привет, ну и зачем ты запросил {slug} ?')
# Create your views here.
