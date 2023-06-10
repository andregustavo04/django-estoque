
"""
URL configuration for estoque project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    # Home
    path('', views.home, name="home"),

    # Adicionar Produtos
    path('adicionar', views.adicionar, name="adicionar"),

    # Ver Produto Individualmente
    path('produto/<str:id>', views.ver_produto, name="ver_produto"),

    # Editar Produto
    path('editar', views.editar_produto, name="editar"),

    # Deletar Produto
    path('deletar/<str:id>', views.deletar_produto, name="deletar"),

    # Login
    path('login', views.loginUser, name="login"),

    # Criar Conta
    path('register', views.registerUser, name="register"),

    # Logout
    path('logout', views.logoutUser, name='logout'),

]

urlpatterns += staticfiles_urlpatterns()