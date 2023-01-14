from rest_framework import  viewsets
from rest_framework.generics import ListAPIView
from .models import Department, Personnel
from .serializers import DepartmentSerializer, DepartmentPersonalSerializer, PersonnelSerializer 
from .permissions import IsStaffOrReadOnly

class DepartmentView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (IsStaffOrReadOnly,)
    
class DepartmentPersonalView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentPersonalSerializer
    permission_classes = (IsStaffOrReadOnly,)
    lookup_field = "name"
    
class PersonnelView(viewsets.ModelViewSet):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
    permission_classes = (IsStaffOrReadOnly,)