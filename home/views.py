from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Generic
from .models import Solution
from .models import Product

# Create your views here.
def index(request):
	generic_list = Generic.objects.order_by('generic_name')[:10]
	solution_list = Solution.objects.order_by('solution_name')
	context = {
		'generic_list': generic_list,
		'solution_list': solution_list,
	}
	return render(request, 'home/index.html', context)

def show_solution(request, generic_id):
	generic = get_object_or_404(Generic, pk=generic_id)
	generic_list = Generic.objects.order_by('generic_name')[:10]
	solution_list = Solution.objects.order_by('solution_name')
	context = {
		'generic_list': generic_list,
		'solution_list': solution_list,
		'generic' : generic,
	}
	return render(request, 'home/show_solution.html', context)
	
def show_product(request, generic_id, solution_id):
	solution = get_object_or_404(Solution, pk=solution_id)
	generic = get_object_or_404(Generic, pk=solution.generic.id)
	generic_list = Generic.objects.order_by('generic_name')
	solution_list = Solution.objects.order_by('solution_name')
	product_list = Product.objects.order_by('product_name')
	context = {
		'generic_list': generic_list,
		'solution_list': solution_list,
		'product_list': product_list,
		'generic': generic,
		'solution': solution,
	}
	return render(request, 'home/show_product.html', context)

def product_detail(request, generic_id, solution_id, product_id):
	product = get_object_or_404(Product, pk=product_id)
	solution = get_object_or_404(Solution, pk=solution_id)
	generic = get_object_or_404(Generic, pk=solution.generic.id)
	generic_list = Generic.objects.order_by('generic_name')
	solution_list = Solution.objects.order_by('solution_name')
	product_list = Product.objects.order_by('product_name')
	context = {
		'generic_list': generic_list,
		'solution_list': solution_list,
		'product_list': product_list,
		'generic': generic,
		'solution': solution,
		'product': product,
	}
	return render(request, 'home/product_detail.html', context)	