from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('about-us', views.about_page),
    path('contacts', views.contact_page),
    path('category/<str:pk>', views.category_page),
    path('product/<int:pk>', views.product_page),
    path('search', views.search_product),
    path('del_item/<int:pk>', views.del_from_cart),
]