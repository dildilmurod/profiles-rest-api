from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers


class HelloApiView(APIView):
    """Test api view"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        apiv = [
            'Uses HTTP methods as function',
            'Similar to Django view',
            'Gives you most logic'
        ]
        return Response({'message': 'Hello', 'apiview': apiv})

    def post(self, request):
        """Create a hello message with name"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)  # adds name to string
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating"""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Patch updates only field provided in the request"""
        return Response({'method': 'patch'})

    def delete(self,request, pk=None):
        """Delete"""

        return Response({'method': 'delete'})