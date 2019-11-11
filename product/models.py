from django.db import models

# Create your models here.


class Location(models.Model):
	loc_id = models.AutoField(primary_key=True)
	loc_name = models.CharField(max_length=100)

	def __str__(self):
		return self.loc_name
	

class Department(models.Model):
	dept_id = models.AutoField(primary_key=True)
	dept_name = models.CharField(max_length=100)
	location_id = models.ForeignKey(Location,related_name='loc_department',on_delete=models.PROTECT)

	def __str__(self):
		return self.dept_name
		
class Category(models.Model):
	cate_id = models.AutoField(primary_key=True)
	cate_name = models.CharField(max_length=100)
	department_id = models.ForeignKey(Department,related_name='dept_category',on_delete=models.PROTECT)

	def __str__(self):
		return self.cate_name

class SubCategory(models.Model):
	sub_cate_id = models.AutoField(primary_key=True)
	sub_cate_name = models.CharField(max_length=100)
	category_id = models.ForeignKey(Category,related_name='cate_subcategory',on_delete=models.PROTECT)

	def __str__(self):
		return self.sub_cate_name	

class SkuDetails(models.Model):
	sku_id = models.AutoField(primary_key=True)
	sku_name = models.CharField(max_length=100)
	location_id = models.ForeignKey(Location,related_name='location_skudetails',on_delete=models.PROTECT)
	department_id = models.ForeignKey(Department,related_name='department_skudetails',on_delete=models.PROTECT)
	category_id = models.ForeignKey(Category,related_name='category_skudetails',on_delete=models.PROTECT)
	sub_category_id = models.ForeignKey(SubCategory,related_name='subcategory_skudetails',on_delete=models.PROTECT)
	
	def __str__(self):
		return self.sku_name
