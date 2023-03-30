from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
    DepartmentViewSet
)

departments_router = SimpleRouter()
departments_router.register('departments', DepartmentViewSet)

urlpatterns = [
    path('departments/', DepartmentViewSet, name='departments'),
    path('departments/<int:pk>', DepartmentViewSet, name='department'),
]
