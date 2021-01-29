from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models
from . import permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles listing, creating and updating"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """User the ObtainAuthToken Apiview to validate and create a token"""
        return ObtainAuthToken().post(request)


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles crud profile feed items"""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        """sets the user profile to the logged in user"""

        serializer.save(user_profile=self.request.user)


# ---------------------


class HelloViewSets(viewsets.ViewSet):
    """Test api viewsets"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """return a hello message"""
        ahello = [
            'Users actions (list, create, retrieve, update, partial_update)',
            'automatically maps to urls using routers',
            'provides more func wiht less code'
        ]
        return Response({'message': 'Hello!', 'ahello': ahello})

    def create(self, request):
        """Create a new record"""
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """get by id"""
        return Response({'method': 'GET (by id)'})

    def update(self, request, pk=None):
        """updating"""
        return Response({'method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Update provided fields"""
        return Response({'method': 'PATCH'})

    def destroy(self, requst, pk=None):
        """Delete"""
        return Response({'method': 'DELETE'})


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

    def delete(self, request, pk=None):
        """Delete"""

        return Response({'method': 'delete'})
