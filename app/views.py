from django.shortcuts import render
from django.views.generic import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TodoModel
from .serializers import TodoSerializer
from rest_framework import status

class HomeView(APIView):

    def get(self, request):
        qs = TodoModel.objects.filter(status=False)
        s = TodoSerializer(qs, many=True)
        return Response(s.data)

    def post(self, request):
        serializer =  TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': '404'})

    def delete(self, request, pk):
        object = self.get_object(pk)
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MainView(APIView):

    def get_object(self, pk):
        try:
            return TodoModel.objects.get(pk=pk)
        except TodoModel.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        object = self.get_object(pk)
        serializer = TodoSerializer(object)
        return Response(serializer.data)

    def patch(self, request, pk):
        object = self.get_object(pk)
        serializer = TodoSerializer(object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)



