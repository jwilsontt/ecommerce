from django.shortcuts import render

# Create your views here.

def home(request):

	template = 'products/home.html'
	context = locals()
	return render(request, template, context)