from django.urls import path 
from Employee.View.employee_account_api import (
    EmployeeRegistrationAPI,
    EmployeeLoginAPI,
    LogOutAPI
)

from Employee.View.employee_show import (
    Employee_list_api,
    Employee_update_retrieve_information_api,
    Employee_update_information_API,
    EmployeeDelete_API_view
)


urlpatterns = [
    path('signup/',EmployeeRegistrationAPI.as_view(),name='signup'),
    path('login/',EmployeeLoginAPI.as_view(),name='login'),
    path('logout/',LogOutAPI.as_view(),name='logout'),
    path('list/',Employee_list_api.as_view(),name='all'),
    path('update/<int:pk>',Employee_update_retrieve_information_api.as_view(),name='update'),
    path('list/<int:pk>',Employee_update_retrieve_information_api.as_view(),name='retrieve'),
    path('delete/<int:pk>',EmployeeDelete_API_view.as_view(),name='delete'),

]
