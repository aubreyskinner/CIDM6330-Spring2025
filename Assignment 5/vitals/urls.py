from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CaseManagerViewSet, PatientViewSet, HealthcareProviderViewSet, VitalSignsViewSet
from . import views

router = DefaultRouter()
router.register(r'case_managers', CaseManagerViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'healthcare_providers', HealthcareProviderViewSet)
router.register(r'vital_signs', VitalSignsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('start_task/', views.start_task, name='start_task'),
    path('check_status/<str:task_id>/', views.check_task_status, name='check_task_status'),
]
