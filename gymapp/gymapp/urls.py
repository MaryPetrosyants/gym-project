"""
URL configuration for gymapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from gym.trainer.views import TrainerViewSet, ContractViewSet
from gym.abonement.views import AbonementViewSet
from gym.equipment.views import EquipmentViewSet
from gym.training.views import TrainingViewSet,SignUpForTrainingViewSet





router = DefaultRouter()
router.register(r'trainers', TrainerViewSet)
router.register(r'abonements', AbonementViewSet)
router.register(r'equipment', EquipmentViewSet)
router.register(r'trainings', TrainingViewSet)
router.register(r'signups', SignUpForTrainingViewSet)
router.register(r'contracts', ContractViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('accounts/', include('rest_registration.api.urls')),
]
