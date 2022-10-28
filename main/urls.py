from django.urls import path
# import views do app main
from .views import HomeView
urlpatterns = [
# o nome home é apenas para o desenvolvimento o usuário final não tem acesso
    path('', HomeView.as_view(), name='home')
]