from django.shortcuts import render, redirect 
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms 
from .models import Order
from .forms import ProductFilterForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


def category(request, foo):
    # Replace Hyphens with spaces
    foo = foo.replace('-', ' ')
    # Grab the category from the url
    try:
        # Look Up The Category
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(Category=category)
        return render(request, 'category.html', {'products':products, 'category':category})
    except:
        messages.success(request, ("Cette Categorie n'existe pas... "))
        return redirect('home')   


def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})



def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})



def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Vous-vous êtes connecté"))
            return redirect('home')
        else:
            messages.success(request, ("Il y a une erreure quelque parts, Reéssayez une autre fois "))
            return redirect('login')    
    else:
      return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, (" Vous-vous êtes déconnecté...Merci d'avoir utilisé notre site. "))
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, (" Vous avez créé votre compte avec succés ."))
            return redirect('home')
        else:
            messages.success(request, (" Il y a une erreure quelque parts, Reéssayez une autre fois "))
            return redirect('register')
    else:
       return render(request, 'register.html', {'form':form})
    

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'order_history.html', {'orders': orders})

@login_required
def submit_review(request, product_id):
    # Handle review submission logic here
    pass

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})



def product_list(request):
    form = ProductFilterForm(request.GET)
    products = Product.objects.all()

    if form.is_valid():
        if form.cleaned_data['search']:
            products = products.filter(name__icontains=form.cleaned_data['search'])
        if form.cleaned_data['min_price']:
            products = products.filter(price__gte=form.cleaned_data['min_price'])
        if form.cleaned_data['max_price']:
            products = products.filter(price__lte=form.cleaned_data['max_price'])
        if form.cleaned_data['brand']:
            products = products.filter(brand__icontains=form.cleaned_data['brand'])
        if form.cleaned_data['model']:
            products = products.filter(model__icontains=form.cleaned_data['model'])

    return render(request, 'Piecesstore/product_list.html', {'form': form, 'products': products})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Review
from .forms import ReviewForm

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ReviewForm()
    return render(request, 'Piecesstore/product_detail.html', {'product': product, 'reviews': reviews, 'form': form})


    