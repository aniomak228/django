from django.shortcuts import render, redirect
from django.views.generic import DetailView
from news.models import Articles
from .forms import ArticlesForm



def news_index(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/index.html', {'news': news})

class NewsDetail(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Некоректне заповнення'
            

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)