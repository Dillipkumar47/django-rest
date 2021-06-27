from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from  .serializer import StudentSerializer
# Create your views here.

class studentView(APIView):
    def get(self, request):
        query = Student.objects.all()
        serializer = StudentSerializer(query, many=True)    
        return Response(serializer.data, status=200)