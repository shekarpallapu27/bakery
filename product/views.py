from django.shortcuts import render

# Create your views here.

from .serializers import *
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *

import traceback
import logging
product_logger = logging.getLogger('product')
product_except_logger = logging.getLogger('product_except')

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


def index(request):
    try:
        if request.method=="GET":
            if request.user.is_authenticated():
                return HttpResponseRedirect('/dashboard/')
            return render(request,'index.html')
        else:
            username = request.POST.get('uname', '')
            password = request.POST.get('psw', '')
            user = auth.authenticate(username = username, password = password)       
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect('/dashboard/')
            else:
                return render(request,'index.html')
    except Exception as er:
        product_except_logger.critical(
            str(er) + '\n' + str(traceback.format_exc()))

@login_required
def user_logout(request):
    try:
        auth.logout(request)
        return HttpResponseRedirect('/')
    except Exception as er:
        product_except_logger.critical(
            str(er) + '\n' + str(traceback.format_exc()))


def dashboard(request):
    try:
        return render(request,'dashborad.html')
    except Exception as er:
        product_except_logger.critical(
            str(er) + '\n' + str(traceback.format_exc()))

class LocationDetails(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        try:
            loc_id =request.GET.get('loc_id')
            if loc_id:
                loc_obj = Location.objects.filter(pk=loc_id)
            else:
                loc_obj = Location.objects.all()
            obj = LocationSerializer(loc_obj,many=True)
            product_logger.info("Viewing content for Location Details ")
            return Response(obj.data)
        except Exception as er:
            product_except_logger.critical(
                str(er) + '\n' + str(traceback.format_exc()))
            return Response("Failed")

    def post(self,request):
        try:
            l_name = request.data[0].get('loc_name')
            Location.objects.create(loc_name=l_name)
            product_logger.info("Created content for Location Details ")
            return Response('Saved Successfully')
        except Exception as er:
            product_except_logger.critical(
                str(er) + '\n' + str(traceback.format_exc()))
            return Response("Failed")
    def put(self,request):
        try:
            loc_id = request.data[0].get('loc_id')
            l_name = request.data[0].get('loc_name')
            update_loc = Location.objects.filter(pk = loc_id)
            update_loc.update(loc_name=l_name)
            product_logger.info("Updating the content for Location Details ")
            return Response('Updated Successfully')
        except Exception as er:
            product_except_logger.critical(
                str(er) + '\n' + str(traceback.format_exc()))
            return Response("Failed")
    def delete(self,request):
        try:
            loc_id =request.GET.get('loc_id')
            Location.objects.filter(pk=loc_id).delete()
            product_logger.info("Deleted the content for Location Details ")
            return Response('Deleted Successfully')
        except Exception as er:
            product_except_logger.critical(
                str(er) + '\n' + str(traceback.format_exc()))
            return Response("Failed")




class DepartmentDetails(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        try:
            dept_id =request.GET.get('dept_id')
            dept_loc_id =request.GET.get('dept_loc_id')
            location_id =request.GET.get('location_id')
            if dept_id:
                dept_obj = Department.objects.filter(pk=dept_id)
            elif dept_loc_id:
                dept_obj = Department.objects.filter(location_id__pk=dept_loc_id)
            elif location_id:
                dept_obj = Department.objects.filter(location_id__pk=location_id)
            else:
                dept_obj = Department.objects.all()
            obj = DepartmentSerializer(dept_obj,many=True)
            product_logger.info("Viewing content for Department Details ")
            return Response(obj.data)
        except Exception as er:
            product_except_logger.critical(
                str(er) + '\n' + str(traceback.format_exc()))
            return Response("Failed")
    def post(self,request):
        try:
            d_name = request.data[0].get('dept_name')
            loc_id = request.data[0].get('loc_id')
            dept_loc_obj = Location.objects.get(pk=loc_id)
            Department.objects.create(dept_name=d_name,location_id=dept_loc_obj)
            product_logger.info("Created the content for Department Details ")
            return Response('Created Successfully')
        except Exception as er:
            product_except_logger.critical(
                str(er) + '\n' + str(traceback.format_exc()))
            return Response("Failed")
    def put(self,request):
        try:
            dept_id = request.data[0].get('dept_id')
            d_name = request.data[0].get('dept_name')
            update_dept = Department.objects.filter(pk = dept_id)
            update_dept.update(dept_name=d_name)
            product_logger.info("Updated the content for Department Details ")
            return Response('Updated Successfully')
        except Exception as er:
            product_except_logger.critical(
                str(er) + '\n' + str(traceback.format_exc()))
            return Response("Failed")
    def delete(self,request):
        try:
            dept_id =request.GET.get('dept_id')
            Department.objects.filter(pk=dept_id).delete()
            product_logger.info("Deleted the content for Department Details ")
            return Response('Deleted Successfully')
        except Exception as er:
            product_except_logger.critical(
                str(er) + '\n' + str(traceback.format_exc()))
            return Response("Failed")

class CategoryDetails(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        try:
            cate_id =request.GET.get('cate_id')
            cate_dept_id =request.GET.get('cate_dept_id')
            locc_id =request.GET.get('location_id')
            deparr_id =request.GET.get('department_id')

            if cate_id:
                cate_obj = Category.objects.filter(pk=cate_id)
            elif cate_dept_id:
                cate_obj = Category.objects.filter(department_id__pk=cate_dept_id)
            elif locc_id and deparr_id:
                cate_obj = Category.objects.filter(department_id__location_id__pk=locc_id,department_id__pk=deparr_id)
            else:
                cate_obj = Category.objects.all()
            obj = CategorySerializer(cate_obj,many=True)
            product_logger.info("Viewing content for Category Details ")
            return Response(obj.data)
        except Exception as er:
            product_except_logger.critical(
                str(er) + '\n' + str(traceback.format_exc()))
            return Response("Failed")

    def post(self,request):
        try:
            c_name = request.data[0].get('cate_name')
            dept_id = request.data[0].get('dept_id')
            dept_obj = Department.objects.get(pk=dept_id)
            Category.objects.create(cate_name=c_name,department_id=dept_obj)
            product_logger.info("Created the content for Category Details ")
            return Response('Created Successfully')
        except Exception as er:
            product_except_logger.critical(
                str(er) + '\n' + str(traceback.format_exc()))
            return Response("Failed")
    def put(self,request):
        try:
            cate_id = request.data[0].get('cate_id')
            c_name = request.data[0].get('cate_name')
            update_cate = Category.objects.filter(pk = cate_id)
            update_cate.update(cate_name=c_name)
            product_logger.info("Updated the content for Category Details ")
            return Response('Updated Successfully')
        except Exception as er:
            product_except_logger.critical(
                str(er) + '\n' + str(traceback.format_exc()))
            return Response("Failed")

    def delete(self,request):
        try:
            cate_id =request.GET.get('cate_id')
            Category.objects.filter(pk=cate_id).delete()
            product_logger.info("Deleted the content for Category Details ")
            return Response('Deleted Successfully')
        except Exception as er:
            product_except_logger.critical(
                str(er) + '\n' + str(traceback.format_exc()))
            return Response("Failed")


class SubCategoryDetails(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        try:
            sub_cate_id =request.GET.get('sub_cate_id')
            subcate_cate_id =request.GET.get('subcate_cate_id')
            locc_id =request.GET.get('location_id')
            deparr_id =request.GET.get('department_id')
            catee_id = request.GET.get('category_id')
            if sub_cate_id:
                sub_cate_obj = SubCategory.objects.filter(pk=sub_cate_id)
            elif subcate_cate_id:
                sub_cate_obj = SubCategory.objects.filter(category_id__pk=subcate_cate_id)
            elif locc_id and deparr_id and catee_id:
                sub_cate_obj = SubCategory.objects.filter(category_id__department_id__location_id__pk=locc_id,category_id__department_id__pk=deparr_id,category_id__pk=catee_id)
            else:
                sub_cate_obj = SubCategory.objects.all()
            obj = SubCategorySerializer(sub_cate_obj,many=True)
            product_logger.info("Viewing content for SubCategory Details ")
            return Response(obj.data)
        except Exception as er:
            product_except_logger.critical(
                str(er) + '\n' + str(traceback.format_exc()))
            return Response("Failed")

    def post(self,request):
        try:
            sub_cate_name = request.data[0].get('sub_cate_name')
            cate_id = request.data[0].get('cate_id')
            cate_obj = Category.objects.get(pk=cate_id)
            SubCategory.objects.create(sub_cate_name=sub_cate_name,category_id=cate_obj)
            product_logger.info("Created content for SubCategory Details ")
            return Response('Saved Successfully')
        except Exception as er:
            product_except_logger.critical(
                str(er) + '\n' + str(traceback.format_exc()))
            return Response("Failed")
    def put(self,request):
        try:
            sub_cate_id = request.data[0].get('sub_cate_id')
            sub_cate_name = request.data[0].get('sub_cate_name')
            update_sub_cate = SubCategory.objects.filter(pk = sub_cate_id)
            update_sub_cate.update(sub_cate_name=sub_cate_name)
            product_logger.info("Updated content for SubCategory Details ")
            return Response('Updated Successfully')
        except Exception as er:
            product_except_logger.critical(
                str(er) + '\n' + str(traceback.format_exc()))
            return Response("Failed")
    def delete(self,request):
        try:
            sub_cate_id =request.GET.get('sub_cate_id')
            SubCategory.objects.filter(pk=sub_cate_id).delete()
            product_logger.info("Deleted the content for SubCategory Details ")
            return Response('Deleted Successfully')
        except Exception as er:
            product_except_logger.critical(
                str(er) + '\n' + str(traceback.format_exc()))
            return Response("Failed")




class SkuDataDetails(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        try:
            sku_id =request.GET.get('sku_id')
            locc_id =request.GET.get('location_id')
            deparr_id =request.GET.get('department_id')
            catee_id = request.GET.get('category_id')
            subcatee_id = request.GET.get('subcategory_id')

            if sku_id:
                sku_obj = SkuDetails.objects.filter(pk=sku_id)
            elif locc_id and deparr_id and catee_id and subcatee_id:
                sku_obj = SkuDetails.objects.filter(sub_category_id__category_id__department_id__location_id__pk=locc_id,sub_category_id__category_id__department_id__pk=deparr_id,sub_category_id__category_id__pk=catee_id,sub_category_id__pk=subcatee_id)
            else:
                sku_obj = SkuDetails.objects.all()
            obj = SkuSerializer(sku_obj,many=True)
            product_logger.info("Viewing content for SkuDetails Details ")
            return Response(obj.data)
        except Exception as er:
            product_except_logger.critical(
                str(er) + '\n' + str(traceback.format_exc()))
            return Response("Failed")

    def post(self,request):
        try:
            loc_id = request.data[0].get('loc_id')
            dept_id = request.data[0].get('dept_id')
            cate_id = request.data[0].get('cate_id')
            sub_cate_id = request.data[0].get('sub_cate_id')
            sku_name = request.data[0].get('sku_name')
            loc_obj = Location.objects.get(pk=loc_id)
            dept_obj = Department.objects.get(pk=dept_id)
            cate_obj = Category.objects.get(pk=cate_id)
            subcate_obj = SubCategory.objects.get(pk=sub_cate_id)
            SkuDetails.objects.create(sku_name=sku_name,location_id=loc_obj,department_id=dept_obj,category_id=cate_obj,sub_category_id=subcate_obj)
            product_logger.info("Created content for SkuDetails Details ")
            return Response('Saved Successfully')
        except Exception as er:
            product_except_logger.critical(
                str(er) + '\n' + str(traceback.format_exc()))
            return Response("Failed")
    def put(self,request):
        try:
            sku_id = request.data[0].get('sku_id')
            sku_name = request.data[0].get('sku_name')
            update_sku = SkuDetails.objects.filter(pk = sku_id)
            update_sku.update(sku_name=sku_name)
            product_logger.info("Updated content for SkuDetails Details ")
            return Response('Updated Successfully')
        except Exception as er:
            product_except_logger.critical(
                str(er) + '\n' + str(traceback.format_exc()))
            return Response("Failed")
    def delete(self,request):
        try:
            sub_cate_id =request.GET.get('sku_id')
            SkuDetails.objects.filter(pk=sku_id).delete()
            product_logger.info("Deleted the content for SkuDetails Details ")
            return Response('Deleted Successfully')
        except Exception as er:
            product_except_logger.critical(
                str(er) + '\n' + str(traceback.format_exc()))
            return Response("Failed")