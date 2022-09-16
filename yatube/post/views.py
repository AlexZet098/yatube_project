from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    template = 'post/index.html'
    return render(request, template)


def group_posts(request, slug):
    return HttpResponse(f'Группа  {slug}')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def post_detail(request, pk):
    return HttpResponse(f'Пост номер {pk}')
