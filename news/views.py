from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Category
from .forms import NewsForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .utils import MyMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator


def test(request):
    contact_list = ['john', 'lex', 'dima', 'bill',
                    'john1', 'lex1', 'dima1', 'bill1',
                    'john2', 'lex2', 'dima2', 'bill2', 'bill2']
    paginator = Paginator(contact_list, 3)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'news/test.html', {'page_obj': page_obj})


class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'news/home_news.html'
    context_object_name = 'news'
    extra_context = {'title': 'Головна'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Головна'
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news.html'
    context_object_name = 'news'
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context


class ViewNews(DetailView):
    model = News
    # pk_url_kwarg = 'news_id'
    # template_name = 'news/news_detail.html'
    context_object_name = 'news_item'


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('home')


# def index(request):
#     news = News.objects.all()
#
#     title = 'Новости'
#     context = {
#         'title': title,
#         'news': news,
#     }
#     return render(request, 'news/index.html', context)


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     context = {
#         'news': news,
#         'category': category,
#     }
#     return render(request, 'news/category.html', context)


# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     context = {
#         'news_item': news_item,
#     }
#     return render(request, 'news/view_news.html', context)


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             news = form.save()
#             return redirect(news)
#
#     else:
#         form = NewsForm()
#     context = {
#         'form': form,
#         }
#     return render(request, 'news/add_news.html', context)





























