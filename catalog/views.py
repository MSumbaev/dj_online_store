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
