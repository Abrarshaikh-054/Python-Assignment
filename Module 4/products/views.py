from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

def product_list(request):
    products = ProductMst.objects.prefetch_related('subcategories').all()
    return render(request, 'product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductSubCatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductSubCatForm()
    return render(request, 'add_product.html', {'form': form})

def edit_product(request, pk):
    subcat = get_object_or_404(ProductSubCat, pk=pk)
    if request.method == 'POST':
        form = ProductSubCatForm(request.POST, request.FILES, instance=subcat)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductSubCatForm(instance=subcat)
    return render(request, 'edit_product.html', {'form': form})

def delete_product(request, pk):
    product = get_object_or_404(ProductSubCat, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'delete_product.html', {'product': product})

def search_product(request):
    query = request.GET.get('q')
    products = ProductMst.objects.filter(product_name__icontains=query)
    subcategories = ProductSubCat.objects.filter(product__product_name__icontains=query)
    return render(request, 'search_product.html', {'products': products, 'subcategories': subcategories})
