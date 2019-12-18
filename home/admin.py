from django.contrib import admin
from django import forms
from .models import Generic, Product, Solution

# Register your models here.
class SolutionAdmin(admin.ModelAdmin):
	fieldset = [
		('Description', {'fields': ['solution_desc']})
	]
	
class GenericAdmin(admin.ModelAdmin):
	fieldset = [
		('Description', {'fields': ['generic_desc']})
	]
	
class ProductAdmin(admin.ModelAdmin):
	fieldset = [
		('Description', {'fields': ['product_desc']}),
	]
	
admin.site.register(Generic, GenericAdmin)
admin.site.register(Solution, SolutionAdmin)
admin.site.register(Product, ProductAdmin)