from rest_framework import generics
from .models import Emp
from .serializers import EmpSerializer

class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer

class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer
