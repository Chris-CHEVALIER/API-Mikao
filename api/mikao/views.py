from django.shortcuts import render
from .models import User, Treatment, Symptom, FavoriteList
from rest_framework import viewsets
from .serializers import UserSerializer, TreatmentSerializer, SymptomSerializer, FavoriteListSerializer
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
 
class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class CustomView(APIView):
    def get(self, request, format=None):
        return Response("Some Get Response")
 
    def post(self, request, format=None):
        return Response("Some Post Response")

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TreatmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows treatments to be viewed or edited.
    """
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer

class SymptomViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows symptoms to be viewed or edited.
    """
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer

class FavoriteListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows favorite lists to be viewed or edited.
    """
    queryset = FavoriteList.objects.all()
    serializer_class = FavoriteListSerializer
