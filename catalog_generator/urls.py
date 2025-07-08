from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate-csv/', views.generate_csv, name='generate_csv'),
    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
]