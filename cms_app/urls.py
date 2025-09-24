from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('page/<int:page_id>/', views.page_detail, name='page_detail'),
    path('create/', views.create_page, name='create_page'),
    path('dashboard/', views.admin_dash, name='admin_dash'),
    path('category/<int:category_id>/', views.category_pages, name='category_pages'),
]