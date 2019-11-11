from django.conf.urls import url,include
from django.contrib import admin
from .views import *

urlpatterns = [

    url(r'admin/', admin.site.urls),

    url(r'^$', index),
    url(r'dashboard/$', dashboard),
    url(r'^logout/$', user_logout, name='logout'),

	url(r'api/v1/location/$', LocationDetails.as_view()),
	url(r'api/v1/department/$', DepartmentDetails.as_view()),
	url(r'api/v1/category/$', CategoryDetails.as_view()),
	url(r'api/v1/subcategory/$', SubCategoryDetails.as_view()),
	url(r'api/v1/sku/$', SkuDataDetails.as_view()),

]

