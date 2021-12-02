from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})


def about(request):
    return render(request, "about.html")


def addnew(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/")
            except:
                pass
    else:
        form = ProductForm()
    return render(request, "index.html", {"form": form})


def edit(request, id):
    product = Product.objects.get(id=id)
    return render(request, "edit.html", {"product": product})


def update(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST, instance=Product)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, "edit.html", {"product": product})


def destroy(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("/")
