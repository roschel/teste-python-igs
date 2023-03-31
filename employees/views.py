from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from departments.serializers import DepartmentSerializer


# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    department = DepartmentSerializer(read_only=True)


def list_employees(request):
    employees = Employee.objects.all()
    return render(
        request=request,
        template_name="pages/home.html",
        context={"employees": employees},
    )
