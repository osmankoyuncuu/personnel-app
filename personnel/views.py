from rest_framework import  viewsets
from rest_framework.generics import ListAPIView
from .models import Department, Personnel
from .serializers import DepartmentSerializer, DepartmentPersonalSerializer, PersonnelSerializer 

class DepartmentView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
class DepartmentPersonalView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentPersonalSerializer
    
class PersonnelView(viewsets.ModelViewSet):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer