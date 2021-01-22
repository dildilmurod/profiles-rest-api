from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test api view"""

    def get(self, request, format=None):
        apiv = [
            'Uses HTTP methods as function',
            'Similar to Django view',
            'Gives you most logic'
        ]
        return Response({'message': 'Hello', 'apiview': apiv})
