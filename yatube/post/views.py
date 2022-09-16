from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    template = 'post/index.html'
    title = 'Yatube'
    context = {
        'title': title,
        'text': 'Главная страница'
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'post/group_list.html'
    title = 'Yatube - Groups'
    context = {
        'title': title,
        'text': 'Здесь будет информация о группах проекта Yatube'
    }
    return render(request, template, context)


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def post_detail(request, pk):
    template = 'post/post_detail.html'
    return render(request, template)
