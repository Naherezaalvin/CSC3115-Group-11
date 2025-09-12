from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProgramViewSet, ProjectViewSet, OutcomeViewSet

router = DefaultRouter()
router.register(r"programs", ProgramViewSet, basename="program")
router.register(r"projects", ProjectViewSet, basename="project")
router.register(r"outcomes", OutcomeViewSet, basename="outcome")

urlpatterns = [
    path("api/", include(router.urls)),
]