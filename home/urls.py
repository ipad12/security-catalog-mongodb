from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:generic_id>/', views.show_solution, name='show solution'),
	path('<int:generic_id>/<int:solution_id>/', views.show_product, name='show product'),
	path('<int:generic_id>/<int:solution_id>/<int:product_id>', views.product_detail, name='product detail'),
]
