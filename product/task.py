### Run the script for populating the data

import csv 
import os
####### goto shell ----- python manage.py shell
####### run the below script

from .models import *

path = os.getcwd()
meta_path  = path+'/data/'+'metadata.txt'
data_path = path+'/data/'+'data.txt'


def meta_data():     
   with open(meta_path) as csv_file: 
      csv_reader = csv.reader(csv_file, delimiter=',') 
      line_count = 0 
      for row in csv_reader: 
         if line_count == 0: 
            print('Column names are', ", ".join(row)) 
            line_count += 1 
         else: 
            loc_obj,_ = Location.objects.get_or_create(loc_name=row[0]) 
            dept_obj,_ = Department.objects.get_or_create(dept_name=row[1],location_id=loc_obj) 
            cate_obj,_ = Category.objects.get_or_create(cate_name=row[2],department_id=dept_obj) 
            sub_cate_obj,_ = SubCategory.objects.get_or_create(sub_cate_name=row[3],category_id=cate_obj) 
   return True




def sku_data():
   with open(data_path) as csv_file: 
      csv_reader = csv.reader(csv_file, delimiter=',') 
      line_count = 0 
      for row in csv_reader: 
         if line_count == 0: 
            print('Column names are', ", ".join(row)) 
            line_count += 1 
         else:
            try:
               loc_obj = Location.objects.filter(loc_name=row[2]) 
               dept_obj = Department.objects.filter(dept_name=row[3],location_id__loc_name=loc_obj[0].loc_name) 
               cate_obj = Category.objects.filter(cate_name=row[4],department_id__dept_name=dept_obj[0].dept_name) 
               sub_cate_obj=SubCategory.objects.filter(sub_cate_name=row[5],category_id__cate_name=cate_obj[0].cate_name) 
               sku_obj = SkuDetails.objects.create(sku_name=row[1],
                                                   location_id=loc_obj[0],
                                                   department_id=dept_obj[0],
                                                   category_id=cate_obj[0],
                                                   sub_category_id=sub_cate_obj[0])
               sku_obj.save()
            except:
               pass
   return True