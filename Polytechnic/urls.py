from rest_framework.routers import DefaultRouter
from rest_framework import viewsets 
from django.urls import path,include
from Polytechnic.View.polytechnic_api import (
    LocationAPI_all,
    Polytechnic_list_create,
    Polytechnic_update_retrive,
     
)

from Polytechnic.View.polytechnic_detail_api import Polytechnic_Department_Details_api

router=DefaultRouter()
router.register('location',LocationAPI_all)


urlpatterns = [
    path('location/',include(router.urls)),
    path('add/',Polytechnic_list_create.as_view(),name='add'),  
    path('list/',Polytechnic_list_create.as_view(),name='list'),  
    path('update/<int:pk>/',Polytechnic_update_retrive.as_view(),name='update'),  
    path('retrieve/<int:pk>/',Polytechnic_update_retrive.as_view(),name='retrieve'),
    path('department-polytechnic-deatil/',Polytechnic_Department_Details_api.as_view(),name='department-polytechnic-deatil'), 
    path('department-polytechnic-detail-list/',Polytechnic_Department_Details_api.as_view(),name='department-polytechnic-detail-list'),  
]

