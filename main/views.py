from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        'title': 'главная страница!!!',
        'values': ['some', 'hello', 'azamat'],
        'obj': {
            'car' : 'BMW',
            'age' : 18,
            'hobby' : 'DOTA2'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')


def copycat(request):
    return render(request, 'main/copycat.html')

# Create your views here.
