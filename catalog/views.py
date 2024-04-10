from django.shortcuts import render

from catalog.models import Product


def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
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


def product(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
    }
    return render(request, 'catalog/product.html', context)
