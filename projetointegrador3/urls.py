"""
URL configuration for projetointegrador3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from concessionaria.views import *
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'perfis-cliente', PerfilClienteViewSet)
router.register(r'carros', CarroViewSet)
router.register(r'alugueis', AluguelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', obtain_auth_token, name='api-token'),
    path('api/me/alugueis/', AluguelViewSet.as_view({'get': 'me_alugueis'}), name='me-alugueis'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('historico/perfil/<int:pk>/', historico_perfil, name='historico-perfil'),
    path('login/', login_cliente, name='login-cliente'),
    path('historico/', historico_cliente, name='historico'),

]
