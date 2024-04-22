from django.urls import path,include 
from Category.View.category_api import (
    CategoryKeyAPI,
    CategoryNonKeyAPI
)


urlpatterns = [
    path('list/',CategoryNonKeyAPI.as_view(),name='show_category'),
    path('add/',CategoryNonKeyAPI.as_view(),name='add_category'),
    # path('single_category/<int:pk>',CategoryKeyAPI.as_view(),name='show_single_category'),
    path('update/<int:pk>',CategoryKeyAPI.as_view(),name='update_category'),
    path('delete/<int:pk>',CategoryKeyAPI.as_view(),name='delete_category'),
]

