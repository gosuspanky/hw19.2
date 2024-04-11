from django.shortcuts import render

from catalog.models import Product, Category


def home(request):
    category_list = Category.objects.all()
    context = {
        'object_list': category_list,
        'title': 'Доступные категории товаров'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f'Имя - {name}\n'
              f'Телефон - {phone}\n'
              f'Сообщение: {message}')

    return render(request, 'catalog/contacts.html')


def category_products(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Категория: {category_item.name}'
    }
    return render(request, 'catalog/products.html', context)


def product_description(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'object': product,
    }
    return render(request, 'catalog/product.html', context)
