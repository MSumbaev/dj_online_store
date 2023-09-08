from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView

from catalog.forms import ProductForm, VersionForm, CategoryForm
from catalog.models import Product, Category, Version


class HomeView(TemplateView):
    template_name = 'catalog/home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        context_data['object_list'] = Product.objects.all().order_by('-date_of_last_modification')[:5]
        context_data['title'] = 'SkyStore - главная'
        context_data['product_versions'] = Version.objects.filter(product_id=self.kwargs.get('pk'))

        for object in context_data['object_list']:
            active_version = object.version_set.filter(current_version=True).first()
            if active_version:
                object.active_version_number = active_version.version_number
                object.active_version_title = active_version.version_title
            else:
                object.active_version_number = None
                object.active_version_title = None

        return context_data


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('catalog:category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
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
        context_data['title'] = category_item.title
        context_data['product_versions'] = Version.objects.filter(product_id=self.kwargs.get('pk'))

        for object in context_data['object_list']:
            active_version = object.version_set.filter(current_version=True).first()
            if active_version:
                object.active_version_number = active_version.version_number
                object.active_version_title = active_version.version_title
            else:
                object.active_version_number = None
                object.active_version_title = None

        return context_data


class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        'title': 'SkyStore',
    }


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:category', args=[self.object.category.pk])


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:category', args=[self.object.category.pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


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
