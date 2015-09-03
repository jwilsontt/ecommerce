from django.shortcuts import render
from django.http import Http404

# Create your views here.

from .models import Product, ProductImage

def home(request):
	products = Product.objects.all()
	template = 'products/home.html'
	context = {'products': products}
	return render(request, template, context)

def all(request):
	products = Product.objects.all()
	context = {'products': products}
	template = 'products/all.html'
	return render(request, template, context)

def single(request, slug):
	try:
	    product = Product.objects.get(slug=slug)
	    images = ProductImage.objects.filter(product=product)
	    context = {'product': product, "images": images}
	    template = 'products/single.html'
	    return render(request, template, context)
	except:
		raise Http404('Oops, no product exist')