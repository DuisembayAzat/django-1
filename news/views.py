from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView
# на основе этого класса можно создавать динамические страницы. Например ListView можно вывести записи из
# UpdateView готовый класс из джанго который позволяет обновлять данные

# Create your views here.
def news_home(request):
    news = Articles.objects.all()
    return render(request, 'news/news_home.html', {'news': news})

# news = Articles.objects.order_by('title') подобным образом можно сортировать обьекты
# news = Articles.objects.order_by('-title') тут сортировка в обратном порядке
# news = Articles.objects.order_by('date') тут сортировка по дате публикации
# news = Articles.objects.order_by('date')[:3] ограничивает количество публикации публикации

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class =  ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news'
    template_name = 'news/news-delete.html'

def create(request):
    error = ''

    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'форма была неверной'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)