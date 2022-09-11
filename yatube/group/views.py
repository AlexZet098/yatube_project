from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('Главная страница групп')


def group_list(request):
    return HttpResponse('Список групп постов')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts(request, slug):
    return HttpResponse(f'Группа  {slug}')