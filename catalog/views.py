from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from catalog.models import Product, Category


def home(request):
    product_list = Product.objects.all().order_by('date_of_last_modification')
    context = {
        'object_list': product_list,
        'title': 'Все товары'
    }

    return render(request, 'catalog/home.html', context)


class CategoryCreateView(CreateView):
    model = Category
    fields = ('title', 'description',)
    success_url = reverse_lazy('catalog:category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ('title', 'description',)
    success_url = reverse_lazy('catalog:category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('catalog:category_list')


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории товаров'
    }


class ProductsListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk
        context_data['title'] = category_item.title

        return context_data


class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        'title': 'SkyStore',
    }


class ProductCreateView(CreateView):
    model = Product
    fields = ('title', 'description', 'category', 'image', 'purchase_price')

    def get_success_url(self):
        return reverse('catalog:category', args=[self.object.category.pk])


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('title', 'description', 'category', 'image', 'purchase_price')

    def get_success_url(self):
        return reverse('catalog:category', args=[self.object.category.pk])


class ProductDeleteView(DeleteView):
    model = Product

    def get_success_url(self):
        return reverse('catalog:category', args=[self.object.category.pk])


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'name: {name}\n'
              f'phone: {phone}\n'
              f'message: {message}\n')

    return render(request, 'catalog/contacts.html', context)
