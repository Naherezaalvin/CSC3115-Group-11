from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProgramViewSet

router = DefaultRouter()
router.register(r"programs", ProgramViewSet, basename="program")


urlpatterns = [
    path("api/", include(router.urls)),
]
