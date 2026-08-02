from django.shortcuts import render, redirect

from catalog.models import Product, Category


def index(request):
    return render(request, 'catalog/index.html')


def contact(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        email = requests.POST.get('email')
        message = requests.POST.get('message')
        print(f'{name} ({email}):{message}')
    return render(requests, 'catalog/contacts.html')