from django.urls import path
from productio.rest.views.views import ProductCategoryCreateAPIView





urlpatterns = [
    path('productCategory/',ProductCategoryCreateAPIView.as_view(),name='Product Category')

]