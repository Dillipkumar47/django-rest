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

    def post(self, request):
        
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=201)    
        return Response(serializer.errors, status=401)