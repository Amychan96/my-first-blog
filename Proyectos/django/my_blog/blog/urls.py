# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ruta para la vista principal de blog
    path('generate-pdf/', views.generate_pdf, name='generate_pdf'),
    # Ruta para generar PDF
]
