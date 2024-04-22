from Category.Model.category_model import CategoryModel
from Category.Serializer.category_serializer import CategorySerializer
from rest_framework import generics 


class CategoryNonKeyAPI(generics.ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class=CategorySerializer


class CategoryKeyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class=CategorySerializer