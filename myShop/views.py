from django.shortcuts import render
from .models import Category, Product

# все категории
def categories_view(request):
    categories = Category.objects.all()
    return render(request, 'myShop/categories.html', {'categories': categories})


# все продукты
def products_view(request):
    products = Product.objects.all()
    return render(request, 'myShop/products.html', {'products': products})


# продукты по категории
def category_products_view(request, id):
    products = Product.objects.filter(category_id=id)
    return render(request, 'myShop/category_products.html', {'products': products})