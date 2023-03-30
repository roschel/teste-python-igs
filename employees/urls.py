from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
    EmployeeViewSet
)

employees_router = SimpleRouter()
employees_router.register('employees', EmployeeViewSet)

urlpatterns = [
    path('employees/', EmployeeViewSet, name='employees'),
    path('employees/<int:pk>', EmployeeViewSet, name='employee'),
]
