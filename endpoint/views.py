from http.client import responses
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.

# Student
class StudentView(APIView):
    def get(self, request):
        data = StudentSerializer(Student.objects.all(), many = True)
        return Response(data.data)
    
    def post(self, request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class StudentViewID(APIView):
    def get(self, request, id):
        try:
            data = StudentSerializer(Student.objects.get(id = id))
            return Response(data.data)
        except Student.DoesNotExist:
            return Response({'Message': 'Student not found'}, status = status.HTTP_404_NOT_FOUND)
    
    def put(self, request, id):
        serializer = StudentSerializer(data = request.data, instance = Student.objects.get(id = id))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id):
        try:
            Student.objects.get(id = id).delete()
            return Response({'Message': 'Student deleted successfully'}, status = status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({'Message': 'Student not found'}, status = status.HTTP_404_NOT_FOUND)


# Subject
class SubjectView(APIView):
    def get(self, request):
        data = SubjectSerializer(Subject.objects.all(), many = True)
        return Response(data.data)
    
    def post(self, request):
        serializer = SubjectSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class SubjectViewID(APIView):
    def get(self, request, id):
        try:
            data = SubjectSerializer(Subject.objects.get(id = id))
            return Response(data.data)
        except Subject.DoesNotExist:
            return Response({'Message': 'Subject not found'}, status = status.HTTP_404_NOT_FOUND)
    
    def put(self, request, id):
        serializer = SubjectSerializer(data = request.data, instance = Subject.objects.get(id = id))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id):
        try:
            Subject.objects.get(id = id).delete()
            return Response({'Message': 'Subject deleted successfully'}, status = status.HTTP_200_OK)
        except Subject.DoesNotExist:
            return Response({'Message': 'Subject not found'}, status = status.HTTP_404_NOT_FOUND)

# Parent
class ParentView(APIView):
    def get(self, request):
        data = ParentSerializer(Parent.objects.all(), many = True)
        return Response(data.data)
    
    def post(self, request):
        serializer = ParentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ParentViewID(APIView):
    def get(self, request, id):
        try:
            data = ParentSerializer(Parent.objects.get(id = id))
            return Response(data.data)
        except Parent.DoesNotExist:
            return Response({'Message': 'Parent not found'}, status = status.HTTP_404_NOT_FOUND)
    
    def put(self, request, id):
        serializer = ParentSerializer(data = request.data, instance = Parent.objects.get(id = id))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id):
        try:
            Parent.objects.get(id = id).delete()
            return Response({'Message': 'Parent deleted successfully'}, status = status.HTTP_200_OK)
        except Parent.DoesNotExist:
            return Response({'Message': 'Parent not found'}, status = status.HTTP_404_NOT_FOUND)