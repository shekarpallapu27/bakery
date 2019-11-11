from product.models import *
from rest_framework import serializers




class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields =   '__all__'
        # fields =   ['loc_name']




class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        # fields =   '__all__'
        fields = ['dept_id', 'dept_name', 'location',]
    location = serializers.SerializerMethodField('get_location_name')
    def get_location_name(self, obj):
        return obj.location_id.loc_name


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['cate_id', 'cate_name', 'department',]

    department = serializers.SerializerMethodField('get_department_name')
    def get_department_name(self, obj):
        return obj.department_id.dept_name


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['sub_cate_id', 'sub_cate_name', 'category',]

    category = serializers.SerializerMethodField('get_category_name')
    def get_category_name(self, obj):
        return obj.category_id.cate_name



class SkuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkuDetails
        # fields = ['sku_id', 'sku_name']

        fields = ['sku_id', 'sku_name', 'location', 'department', 'category',  'sub_category',]

    location = serializers.SerializerMethodField('get_location_name')
    def get_location_name(self, obj):
        return obj.location_id.loc_name

    department = serializers.SerializerMethodField('get_department_name')
    def get_department_name(self, obj):
        return obj.department_id.dept_name

    category = serializers.SerializerMethodField('get_category_name')
    def get_category_name(self, obj):
        return obj.category_id.cate_name

    sub_category = serializers.SerializerMethodField('get_subcategory_name')
    def get_subcategory_name(self, obj):
        return obj.sub_category_id.sub_cate_name