from django.urls import path
from Department.View.department_api import (
    department_list_create_api,
    department_update_retrieve_api,
)


urlpatterns = [
    path('list/',department_list_create_api.as_view(),name='department_list'),
    path('add/',department_list_create_api.as_view(),name='add_department'),
    path('update/<int:pk>',department_update_retrieve_api.as_view(),name='update'),
    path('retrieve/<int:pk>',department_update_retrieve_api.as_view(),name='retrieve'),
]
