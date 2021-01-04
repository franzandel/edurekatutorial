from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import employee
from .serializers import employeeSerializer

class employeesView(APIView):
    def get(self, request):
        employees = employee.objects.all()
        serializer = employeeSerializer(employees, many=True)
        return Response(serializer.data)
    def post(self):
        pass
