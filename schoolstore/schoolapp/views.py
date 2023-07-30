from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, InvalidPage


def home(request):
    return render(request, "home.html")

#
# def allProductCat(request, c_slug=None):
#     c_page = None
#     products_list = None
#     if c_slug is not None:
#         c_page = get_object_or_404(Category, slug=c_slug)
#         products_list = Product.objects.all().filter(category=c_page, available=True)
#     else:
#         products_list = Product.objects.all().filter(available=True)
#     paginator = Paginator(products_list, 6)
#     try:
#         page = int(request.GET.get('page', '1'))
#     except:
#         page = 1
#     try:
#         products = paginator.page(page)
#     except (EmptyPage, InvalidPage):
#         products = paginator.page(paginator.num_pages)
#
#     return render(request, "department.html", {'category': c_page, 'products': products})


# def proDetail(request, c_slug, product_slug):
#     try:
#         product = Product.objects.get(category__slug=c_slug, slug=product_slug)
#     except Exception as e:
#         raise e
#     return render(request, 'product.html', {'product': product})


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def newpage(request):
    return render(request, "new_page.html")


def form(request):
    return render(request, "form.html")

def gs(request):
    return render(request, "gs.html")

def com(request):
    return render(request, "com.html")

def arts(request):
    return render(request, "arts.html")

def astro(request):
    return render(request, "astro.html")

def cs(request):
    return render(request, "cs.html")
