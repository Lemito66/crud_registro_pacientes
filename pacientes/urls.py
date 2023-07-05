from django.urls import path, include
from rest_framework import routers
from .views import PacienteView
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r"pacientes", PacienteView, "pacientes")

urlpatterns = [
    path("api/v1/", include(router.urls)), # Get, POST, PUT, DELETE
    path("docs/", include_docs_urls(title="API Pacientes"))
]