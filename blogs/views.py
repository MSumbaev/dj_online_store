from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from blogs.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body', 'preview')
    success_url = reverse_lazy('blogs:blog_list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'body', 'preview')
    success_url = reverse_lazy('blogs:blog_list')


class BlogDetailView(DetailView):
    model = Blog
    extra_context = {
        'title': 'SkyStore',
    }


class BlogListView(ListView):
    model = Blog
    extra_context = {
        'title': 'Статьи'
    }


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs:blog_list')
