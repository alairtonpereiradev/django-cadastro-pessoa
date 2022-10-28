from django.shortcuts import render
# TemplateView é uma classe para criar pagina html default
from django.views.generic import TemplateView

# criando classe que herda o TemplateView
class HomeView(TemplateView):
    template_name = 'main/index.html'
