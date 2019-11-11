#install virtual environament
virtualenv -p python3 bakery_env

#activate virtual environment as bakery_env
source bakery_env/bin/activate

#install required packages

pip install django==1.11.6
pip install djangorestframework



### Run the below script in shell for populating the data

##########        Note: data already populated so no need to execute the scipts functions  #########


python manage.py shell
from product.task import meta_data,sku_data
meta_data()
sku_data()

###open the login page 

http://127.0.0.1:8000/

####   login with below creadential then only you can able to perform CRUD operation on hierarchical

username: admin
password: admin123

#### logout from the application and redirected to login page

http://127.0.0.1:8000/logout
##############  Note: if you logout from the application you can able to access the data


# below API service for accessing the data and implemented the Basicauthentication
# first login throgh the browser then you can access the below API Services

http://127.0.0.1:8000/api/v1/location/
http://127.0.0.1:8000/api/v1/department/?location_id=64
http://127.0.0.1:8000/api/v1/category/?location_id=64&department_id=63
http://127.0.0.1:8000/api/v1/subcategory/?location_id=64&department_id=63&category_id=62
http://127.0.0.1:8000/api/v1/sku/?location_id=64&department_id=63&category_id=62&subcategory_id=62


#####   Implemented the logging framework
if you get any error check the logs


