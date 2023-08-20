from django.shortcuts import render

from catalog.models import Product, Category


def home(request):
    product_list = Product.objects.all()
    categories_list = Category.objects.all()
    context = {
        'object_list': product_list,
        'categories_list': categories_list,
        'title': 'SkyStore'
    }

    return render(request, 'catalog/home.html', context)


def category(request, pk):
    product_list = Product.objects.filter(category_id=pk)
    category_obj = Category.objects.get(pk=pk)
    context = {
        'object_list': product_list,
        'category': category_obj,
        'title': category_obj.title,
    }

    return render(request, 'catalog/category.html', context)


def product(request, pk):
    product_obj = Product.objects.get(pk=pk)
    context = {
        'object': product_obj,
        'title': 'SkyStore',
    }

    return render(request, 'catalog/product.html', context)


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
