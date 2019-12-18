from django.db import models

# Create your models here.

class Generic(models.Model):
	generic_name = models.CharField(max_length=200)
	generic_desc = models.TextField(blank = True, max_length = 128) 
    
	def __str__(self):
		return self.generic_name	

class Solution(models.Model):
	generic = models.ForeignKey(Generic, on_delete=models.CASCADE, null=True)
	solution_name = models.CharField(max_length=200)
	solution_desc = models.TextField(blank = True, max_length = 128)
	
	def __str__(self):
        	return self.solution_name

class Product(models.Model):
	solution = models.ForeignKey(Solution, on_delete=models.CASCADE, null=True)
	product_name = models.CharField(max_length=200, default=" ")
	product_desc = models.TextField(blank = True, max_length = 128)
	product_slide_deck = models.FileField(upload_to='slidedeck/', null=True, blank=True)
	scoping_document = models.FileField(upload_to='scopingdoc/', null=True, blank=True)
	POC_SOW = models.FileField(upload_to='POC_SOW/', null=True, blank=True)
	competitive_information = models.FileField(upload_to='competitiveinfo/', null=True, blank=True)
	datasheet = models.FileField(upload_to='datasheet/', null=True, blank=True)
	
	def __str__(self):
		return self.product_name
		