from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create, name='add_product'),
    path('<int:product_id>', views.detail, name='product_detail'),
    path('inc_vote/<int:product_id>', views.inc_count, name='inc_vote'),
]
