from django.urls import path

from blogs.apps import BlogsConfig
from blogs.views import BlogCreateView, BlogListView, BlogDetailView, BlogDeleteView, BlogUpdateView

app_name = BlogsConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('update/<int:pk>', BlogUpdateView.as_view(), name='blog_update'),
    path('list/', BlogListView.as_view(), name='blog_list'),
    path('view/<int:pk>', BlogDetailView.as_view(), name='blog_detail_view'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
]
