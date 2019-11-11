var app = angular.module('myApp',  []);

app.config(function($interpolateProvider,$httpProvider){
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $interpolateProvider.startSymbol('[[')
    $interpolateProvider.endSymbol(']]')
});

// app.config(function($httpProvider) {
//     $httpProvider.defaults.common['Authorization'] = token;
//     // For angular 1.5, use:  
//     // $httpProvider.defaults.headers.common['Authorization'] = token;        
// });

 app.controller('ProductController', function($scope,$http,$timeout) {

            $scope.locationn = false;
            $scope.departmentt = false;
            $scope.categoryy = false;

            $scope.subcategoryy = false;
            $scope.sku = false;


            $http.get("/api/v1/location/").then(function(response){
                        $scope.mylocation = response.data
                  });

            $scope.sdepartments = function(dept_loc_id){
                                                    //debugger
                                                    $scope.dept_loc_id = dept_loc_id
                                                    $http({
                                                              url: "/api/v1/department/", 
                                                              method: "GET",
                                                              params: {"dept_loc_id": $scope.dept_loc_id}
                                                           }).then(function successCallback(response) {
                                                                   $scope.mydepartment = response.data

                                                        }, function errorCallback(response) {
                                                              console.log("Error code");
                                                    });
                                            }


            $scope.scategorys = function(cate_dept_id){
                                                    //debugger
                                                    $scope.cate_dept_id = cate_dept_id
                                                    $http({
                                                              url: "/api/v1/category/", 
                                                              method: "GET",
                                                              params: {"cate_dept_id" : $scope.cate_dept_id}
                                                           }).then(function successCallback(response) {
                                                                   $scope.mycategory = response.data

                                                        }, function errorCallback(response) {
                                                              console.log("Error code");
                                                    });
                                            }


            $scope.ssubcates = function(subcate_cate_id){
                                                    //debugger
                                                    $scope.subcate_cate_id = subcate_cate_id
                                                    $http({
                                                              url: "/api/v1/subcategory/", 
                                                              method: "GET",
                                                              params: {"subcate_cate_id" : $scope.subcate_cate_id}
                                                           }).then(function successCallback(response) {
                                                                   $scope.mysubcategory = response.data

                                                        }, function errorCallback(response) {
                                                              console.log("Error code");
                                                    });
                                            }






            $scope.location_data = function(){
                                                $http.get("/api/v1/location/").then(function(response){
                                                  $scope.location = response.data
                                                  $scope.locationn = true;
                                                  $scope.departmentt = false;
                                                  $scope.categoryy = false;
                                                  $scope.subcategoryy = false;
                                                  $scope.sku = false;

                                                });

                                            }

            $scope.add_loc = function(){





                                           $scope.loc_data= [{ 
                                                        "loc_code" : $scope.add_loc_code,
                                                        "loc_name" : $scope.add_loc_name
                                                  }]
                                            $http({
                                                    url: "/api/v1/location/",
                                                    method: "POST",
                                                    data: $scope.loc_data,
                                                    }).then(function successCallback(response) {
                                                                  $scope.add_loc_code = ""
                                                                  $scope.add_loc_name = ""
                                                                $('#addLocationModal').modal('hide');
                                                                 $scope.location_data()
                                                            }, function errorCallback(response) {
                                                                  console.log("Error code");
                                                        }
                                                    );
                    
                                        }

            $scope.edit_loc = function(loc_id){
                                                    $scope.loc_id = loc_id
                                                    $http({
                                                              url: "/api/v1/location/", 
                                                              method: "GET",
                                                              params: {loc_id: loc_id}
                                                           }).then(function successCallback(response) {
                                                                   $scope.edit_location = response.data[0]
                                                                  $('#editLocationModals').modal('show');
                                                                  $scope.location_data()
                                                        }, function errorCallback(response) {

                                                              console.log("Error code");
                                                    });
                                                }

            $scope.update_loc = function(){
                                             $scope.loc_data= [{ 
                                                          "loc_id" : $scope.edit_location.loc_id,
                                                          "loc_code" : $scope.edit_location.loc_code,
                                                          "loc_name" : $scope.edit_location.loc_name
                                                    }]
                                              $http({
                                                      url: "/api/v1/location/",
                                                      method: "PUT",
                                                      data: $scope.loc_data,
                                                      }).then(function successCallback(response) {
                                                                  $('#editLocationModals').modal('hide');
                                                                  $scope.location_data()
                                                              }, function errorCallback(response) {

                                                                    console.log("Error code");
                                                          }
                                                      );
                                          }
            $scope.delete_loc = function(loc_id){
                                                    // debugger
                                                    $scope.loc_id = loc_id
                                                    $http({
                                                              url: "/api/v1/location/", 
                                                              method: "DELETE",
                                                              params: {loc_id: loc_id}
                                                           }).then(function successCallback(response) {
                                                                  // debugger
                                                                  if (response.data=="Failed"){
                                                                    alert("Cannot delete some instances of model 'Location' because they are referenced through a protected foreign key")
                                                                  }
                                                                  else{
                                                                      $scope.location_data()
                                                                      console.log("Success code");
                                                                  }
                                                        }, function errorCallback(response) {
                                                              alert("Cannot delete some instances of model 'Location' because they are referenced through a protected foreign key")
                                                              console.log("Error code");
                                                    });
                                                 }




////////////Department


            $scope.department_data = function(){
                                                $http.get("/api/v1/department/").then(function(response){
                                                  $scope.department = response.data
                                                  
                                                  
                                                  $scope.locationn = false;
                                                  $scope.categoryy = false;
                                                  $scope.subcategoryy = false;
                                                  $scope.departmentt = true;
                                                  $scope.sku = false;

                                                });

                                            }

            $scope.add_department = function(){
                                           $scope.dept_data= [{ 
                                                       "loc_id" : $scope.mylocaaa.loc_id,
                                                        "dept_code" : $scope.add_dept_code,
                                                        "dept_name" : $scope.add_dept_name
                                                  }]
                                            $http({
                                                    url: "/api/v1/department/",
                                                    method: "POST",
                                                    data: $scope.dept_data,
                                                    }).then(function successCallback(response) {
                                                                $scope.mylocaaa = ""
                                                                $scope.add_dept_code = ""
                                                                $scope.add_dept_name = ""
                                                                $('#addDepartmentModal').modal('hide');
                                                                 $scope.department_data()
                                                            }, function errorCallback(response) {
                                                                  console.log("Error code");
                                                        }
                                                    );
                    
                                        }

            $scope.edit_department = function(dept_id,loc_id){

                                                    $scope.dept_id = dept_id
                                                    $http({
                                                              url: "/api/v1/department/", 
                                                              method: "GET",
                                                              params: {dept_id: dept_id}
                                                           }).then(function successCallback(response) {
                                                                     //debugger
                                                                   $scope.edit_dept = response.data[0]
                                                                   //$scope.mydeptlocaaa = response.data[0].location
                                                                  $('#editDepartmentModals').modal('show');
                                                                  $scope.department_data()
                                                        }, function errorCallback(response) {
                                                              console.log("Error code");
                                                    });
                                                }

            $scope.update_department = function(){
                                              //debugger
                                             $scope.dept_data= [{ 
                                             
                                                          "dept_id" : $scope.edit_dept.dept_id,
                                                          "dept_code" : $scope.edit_dept.dept_code,
                                                          "dept_name" : $scope.edit_dept.dept_name
                                                    }]
                                              $http({
                                                      url: "/api/v1/department/",
                                                      method: "PUT",
                                                      data: $scope.dept_data,
                                                      }).then(function successCallback(response) {
                                                                  $('#editDepartmentModals').modal('hide');
                                                                  $scope.department_data()
                                                              }, function errorCallback(response) {
                                                                    console.log("Error code");
                                                          }
                                                      );
                                          }
            $scope.delete_department = function(dept_id){
                                                    $scope.dept_id = dept_id
                                                    $http({
                                                              url: "/api/v1/department/", 
                                                              method: "DELETE",
                                                              params: {dept_id: dept_id}
                                                           }).then(function successCallback(response) {
                                                                  if (response.data=="Failed"){
                                                                    alert("Cannot delete some instances of model 'Department' because they are referenced through a protected foreign key")
                                                                  }
                                                                  else{
                                                                  $scope.department_data()
                                                                }
                                                        }, function errorCallback(response) {
                                                              alert("Cannot delete some instances of model 'Department' because they are referenced through a protected foreign key")
                                                              console.log("Error code");
                                                    });
                                                 }



/////////////Category

            $scope.category_data = function(){
                                                $http.get("/api/v1/category/").then(function(response){
                                                  $scope.category = response.data
                                                  $scope.departmentt = false;
                                                  $scope.locationn = false;
                                                  $scope.categoryy = true;
                                                  $scope.subcategoryy = false;
                                                  $scope.sku = false;

                                                });

                                            }

            $scope.add_category = function(){
                                                //debugger
                                           $scope.cate_data= [{ 
                                                        "dept_id" : $scope.mydepttt.dept_id,
                                                        "cate_code" : $scope.add_cate_code,
                                                        "cate_name" : $scope.add_cate_name
                                                  }]
                                            $http({
                                                    url: "/api/v1/category/",
                                                    method: "POST",
                                                    data: $scope.cate_data,
                                                    }).then(function successCallback(response) {
                                                                  $scope.mylocaaa = ""
                                                                  $scope.mydepttt = ""                                    
                                                                  $scope.add_cate_code = ""
                                                                  $scope.add_cate_name = ""
                                                                $('#addCategoryModal').modal('hide');
                                                                 $scope.category_data()


                                                            }, function errorCallback(response) {
                                                                  console.log("Error code");
                                                        }
                                           
                                                    );
                    
                                        }

            $scope.edit_category = function(cate_id){

                                                    $scope.cate_id = cate_id
                                                    $http({
                                                              url: "/api/v1/category/", 
                                                              method: "GET",
                                                              params: {cate_id: cate_id}
                                                           }).then(function successCallback(response) {
                                                                   $scope.edit_cate = response.data[0]
                                                                  $('#editCategoryModals').modal('show');
                                                                  $scope.category_data()
                                                        }, function errorCallback(response) {
                                                              console.log("Error code");
                                                    });
                                                }

            $scope.update_category = function(){
                                                //debugger
                                             $scope.up_cate_data= [{ 
                                                          "cate_id" : $scope.edit_cate.cate_id,
                                                          "cate_code" : $scope.edit_cate.cate_name,
                                                          "cate_name" : $scope.edit_cate.cate_name
                                                    }]
                                              $http({
                                                      url: "/api/v1/category/",
                                                      method: "PUT",
                                                      data: $scope.up_cate_data,
                                                      }).then(function successCallback(response) {
                                                                  $('#editCategoryModals').modal('hide');
                                                                  $scope.category_data()
                                                              }, function errorCallback(response) {
                                                                    console.log("Error code");
                                                          }
                                                      );
                                          }
            $scope.delete_category = function(cate_id){
                                                    $scope.cate_id = cate_id
                                                    $http({
                                                              url: "/api/v1/category/", 
                                                              method: "DELETE",
                                                              params: {cate_id: cate_id}
                                                           }).then(function successCallback(response) {
                                                                  if (response.data=="Failed"){
                                                                    alert("Cannot delete some instances of model 'Category' because they are referenced through a protected foreign key")
                                                                  }
                                                                  else{
                                                                        $scope.category_data()
                                                                }
                                                        }, function errorCallback(response) {
                                                              alert("Cannot delete some instances of model 'Category' because they are referenced through a protected foreign key")
                                                              console.log("Error code");
                                                    });
                                                 }


  //////////Subcategory




              $scope.subcategory_data = function(){
                                                $http.get("/api/v1/subcategory/").then(function(response){
                                                  $scope.subcategory = response.data
                                                  $scope.departmentt = false;
                                                  $scope.locationn = false;
                                                  $scope.categoryy = false;
                                                  $scope.sku = false;
                                                  $scope.subcategoryy = true;
                                                });

                                            }

            $scope.add_subcategory = function(){
                                           $scope.sub_cate_data= [{ 
                                                        "cate_id" : $scope.mycatttt.cate_id,
                                                        "sub_cate_code" : $scope.add_subcate_code,
                                                        "sub_cate_name" : $scope.add_subcate_name
                                                  }]
                                            $http({
                                                    url: "/api/v1/subcategory/",
                                                    method: "POST",
                                                    data: $scope.sub_cate_data,
                                                    }).then(function successCallback(response) {
                                                                  $scope.mylocaaa = ""
                                                                  $scope.mydepttt = "" 
                                                                  $scope.mycatttt = ""
                                                                  $scope.add_subcate_code = ""
                                                                  $scope.add_subcate_name = ""
                                                                $('#addSubCategoryModal').modal('hide');
                                                                 $scope.subcategory_data()
                                                            }, function errorCallback(response) {
                                                                  console.log("Error code");
                                                        }
                                                    );
                    
                                        }

            $scope.edit_subcategory = function(sub_cate_id){
                                                    $scope.sub_cate_id = sub_cate_id
                                                    $http({
                                                              url: "/api/v1/subcategory/", 
                                                              method: "GET",
                                                              params: {sub_cate_id: sub_cate_id}
                                                           }).then(function successCallback(response) {
                                                                   $scope.edit_sub_cate = response.data[0]
                                                                  $('#editSubCategoryModals').modal('show');
                                                                  $scope.subcategory_data()
                                                        }, function errorCallback(response) {
                                                              console.log("Error code");
                                                    });
                                                }

            $scope.update_subcategory = function(){
                                             $scope.sub_cate_data= [{ 
                                                          "sub_cate_id" : $scope.edit_sub_cate.sub_cate_id,
                                                          "sub_cate_code" : $scope.edit_sub_cate.sub_cate_code,
                                                          "sub_cate_name" : $scope.edit_sub_cate.sub_cate_name
                                                    }]
                                              $http({
                                                      url: "/api/v1/subcategory/",
                                                      method: "PUT",
                                                      data: $scope.sub_cate_data,
                                                      }).then(function successCallback(response) {
                                                                  $('#editSubCategoryModals').modal('hide');
                                                                  $scope.subcategory_data()
                                                              }, function errorCallback(response) {
                                                                    console.log("Error code");
                                                          }
                                                      );
                                          }
            $scope.delete_subcategory = function(sub_cate_id){
                                                    $scope.sub_cate_id = sub_cate_id
                                                    $http({
                                                              url: "/api/v1/subcategory/", 
                                                              method: "DELETE",
                                                              params: {sub_cate_id: sub_cate_id}
                                                           }).then(function successCallback(response) {
                                                                  if (response.data=="Failed"){
                                                                    alert("Cannot delete some instances of model 'SubCategory' because they are referenced through a protected foreign key")
                                                                  }
                                                                  else{
                                                                      $scope.subcategory_data()
                                                                    }
                                                        }, function errorCallback(response) {
                                                              alert("Cannot delete some instances of model 'SubCategory' because they are referenced through a protected foreign key")
                                                              console.log("Error code");
                                                    });
                                                 }



//////Skudetails


              $scope.sku_info = function(){
                                                $http.get("/api/v1/sku/").then(function(response){
                                                  $scope.sku_data = response.data
                                                  $scope.departmentt = false;
                                                  $scope.locationn = false;
                                                  $scope.categoryy = false;
                                                  $scope.subcategoryy = false;
                                                  $scope.sku = true;

                                                });

                                            }

            $scope.add_skudetails = function(){
                                                //debugger
                                           $scope.sku_add= [{ 
                                                        "loc_id" : $scope.mylocaaa.loc_id,
                                                        "dept_id" : $scope.mydepttt.dept_id,
                                                        "cate_id" : $scope.mycatttt.cate_id,                                                        
                                                        "sub_cate_id" : $scope.mysubcateee.sub_cate_id,
                                                        "sku_code" : $scope.add_sku_code,
                                                        "sku_name" : $scope.add_sku_name
                                                  }]
                                            $http({
                                                    url: "/api/v1/sku/",
                                                    method: "POST",
                                                    data: $scope.sku_add,
                                                    }).then(function successCallback(response) {
                                                                  $scope.mylocaaa = ""
                                                                  $scope.mydepttt = "" 
                                                                  $scope.mycatttt = ""
                                                                  $scope.mysubcateee = ""
                                                                  $scope.add_sku_code = ""
                                                                  $scope.add_sku_name = ""
                                                                $('#addSkuModal').modal('hide');
                                                                 $scope.sku_info()
                                                            }, function errorCallback(response) {
                                                                  console.log("Error code");
                                                        }
                                                    );
                    
                                        }

            $scope.edit_skudetails = function(sku_id){
                                                    $scope.sku_id = sku_id
                                                    $http({
                                                              url: "/api/v1/sku/", 
                                                              method: "GET",
                                                              params: {sku_id: sku_id}
                                                           }).then(function successCallback(response) {
                                                                   $scope.edit_sku = response.data[0]
                                                                  $('#editSkuModals').modal('show');
                                                                  $scope.sku_info()
                                                        }, function errorCallback(response) {
                                                              console.log("Error code");
                                                    });
                                                }

            $scope.update_skudetails = function(){
                                             $scope.skuuuu= [{ 
                                                          "sku_id" : $scope.edit_sku.sku_id,
                                                          "sku_code" : $scope.edit_sku.sku_code,
                                                          "sku_name" : $scope.edit_sku.sku_name
                                                    }]
                                              $http({
                                                      url: "/api/v1/sku/",
                                                      method: "PUT",
                                                      data: $scope.skuuuu,
                                                      }).then(function successCallback(response) {
                                                                  $('#editSkuModals').modal('hide');
                                                                  $scope.sku_info()
                                                              }, function errorCallback(response) {
                                                                    console.log("Error code");
                                                          }
                                                      );
                                          }
            $scope.delete_skudetails = function(sku_id){
                                                    $scope.sku_id = sku_id
                                                    $http({
                                                              url: "/api/v1/sku/", 
                                                              method: "DELETE",
                                                              params: {sku_id: sku_id}
                                                           }).then(function successCallback(response) {
                                                                  if (response.data=="Failed"){
                                                                    alert("Cannot delete some instances of model 'SkuDetails' because they are referenced through a protected foreign key")
                                                                  }
                                                                  else{
                                                                      $scope.sku_info()
                                                                    }
                                                        }, function errorCallback(response) {
                                                              alert("Cannot delete some instances of model 'SkuDetails' because they are referenced through a protected foreign key")
                                                              console.log("Error code");
                                                    });
                                                 }

    });